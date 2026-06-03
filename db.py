import asyncio
import psycopg
import os
import psycopg_pool
import contextlib
import psycopg.rows
import bcrypt
#Local import
from config import DATABASE_URL

pool = None

async def init_db():
    global pool
    pool = psycopg_pool.AsyncConnectionPool(DATABASE_URL, min_size=1, max_size=16)

async def close_db():
    await pool.close()
@contextlib.asynccontextmanager
async def getDictCursor():
    """
    Async context manager that yields a cursor returning dict rows.
    """
    async with pool.connection() as aconn:
        async with aconn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            yield cur

async def has_data():
    """
    Checks if core schema exists (not just any table)
    """
    async with getDictCursor() as cur:
        await cur.execute("""
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name = 'user_account'
            );
        """)
        result = await cur.fetchone()
        return result["exists"] if result else False

async def reset_db():
    """
    Drops everything in public schema (tables, types, etc.)
    """
    async with getDictCursor() as cur:
        await cur.execute("""
            DO $$ DECLARE
                r RECORD;
            BEGIN
                -- Drop all tables
                FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
                    EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                END LOOP;

                -- Drop all enums
                FOR r IN (SELECT typname FROM pg_type
                           JOIN pg_namespace n ON n.oid = pg_type.typnamespace
                           WHERE n.nspname = 'public') LOOP
                    EXECUTE 'DROP TYPE IF EXISTS ' || quote_ident(r.typname) || ' CASCADE';
                END LOOP;
            END $$;
        """)


async def execute_script(sql: str):
    """
    Executes raw SQL script (schema.sql)
    """
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)

        await conn.commit()

async def create_default_admin():
    email = "admin@gmail.com"
    username = "admin"
    password = "admin@1234"
    user_role = "sys_admin"
    status = "active"
    first_name = "System"
    last_name = "Admin"

    async with getDictCursor() as cur:
        await cur.execute(
            "SELECT id FROM user_account WHERE username = %s",
            (username,)
        )

        if await cur.fetchone():
            print("Default admin already exists")
            return

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

        await cur.execute(
            """
            INSERT INTO user_info (first_name, last_name)
            VALUES (%s, %s)
            RETURNING id
            """,
            (first_name, last_name)
        )

        user_info_id = (await cur.fetchone())["id"]

        await cur.execute(
            """
            INSERT INTO user_account
            (email, username, hash, user_role, status, user_info_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                email,
                username,
                hashed,
                user_role,
                status,
                user_info_id,
            )
        )

