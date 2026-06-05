import fastapi
import asyncio
import os
import uvicorn

from fastapi.middleware.cors import CORSMiddleware

import datetime

# Local
import db
import routes.login as login
import routes.admin as admin
import routes.user as user
import routes.chats as chats
from config import SETUP

app = fastapi.FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)


# SETUP MODE
async def setup_mode():
    db_exists = await db.has_data()

    if db_exists:
        choice = input("DB exists. Delete and reset? (y/n): ").strip().lower()
        if choice != "y":
            return

    await db.reset_db()
    print("Reset DB complete")

    choice = input("Setup db in fresh environment? (y/n): ").strip().lower()
    if choice != "y":
        return

    try:
        with open("schema.sql", "r") as f:
            sql = f.read()

        await db.execute_script(sql)
        print("DB setup done")

        await db.create_default_admin()
        print("Created a default admin user")

        # Update SETUP=true -> SETUP=false
        with open(".env", "r") as f:
            lines = f.readlines()

        with open(".env", "w") as f:
            for line in lines:
                if line.strip().startswith("SETUP="):
                    f.write("SETUP=false\n")
                else:
                    f.write(line)

        print("Setup complete")

    except Exception as e:
        print(f"Setup failed: {e}")
        raise

@app.on_event("startup")
async def startup():
	await db.init_db()

	if SETUP == "true":
		await setup_mode()


@app.on_event("shutdown")
async def shutdown():
	await db.close_db()



app.include_router(login.router)
app.include_router(admin.router)
app.include_router(user.router)
app.include_router(chats.router)


if __name__ == "__main__":
	uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=False)
