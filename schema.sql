DROP TABLE IF EXISTS message_read CASCADE;
DROP TABLE IF EXISTS message CASCADE;
DROP TABLE IF EXISTS channel_user CASCADE;
DROP TABLE IF EXISTS channel CASCADE;
DROP TABLE IF EXISTS user_account CASCADE;
DROP TABLE IF EXISTS user_info CASCADE;

CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE user_account (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL,
    user_role TEXT NOT NULL,
    status TEXT DEFAULT 'active',
    user_info_id INT REFERENCES user_info(id)
);

CREATE TABLE channel (
    id SERIAL PRIMARY KEY,
    name TEXT,
    status TEXT
);

CREATE TABLE channel_user (
    channel_id INT REFERENCES channel(id),
    user_id INT REFERENCES user_account(id),
    permission BIGINT,
    status TEXT,
    PRIMARY KEY (channel_id, user_id)
);

DO $$ BEGIN
    CREATE TYPE message_status AS ENUM (
        'Normal',
        'Edited',
        'Deleted',
        'Attachment'
    );
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE message (
    id SERIAL PRIMARY KEY,
    channel_id INTEGER REFERENCES channel(id),
    sender INTEGER REFERENCES user_account(id),
    user_account_id INTEGER REFERENCES user_account(id),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    message TEXT,
    status message_status DEFAULT 'Normal',
    prev_message_id INTEGER REFERENCES message(id)
);

CREATE TABLE message_read (
    user_account_id INTEGER REFERENCES user_account(id),
    channel_id INTEGER REFERENCES channel(id),
    last_read_message_id INTEGER REFERENCES message(id),
    PRIMARY KEY (user_account_id, channel_id)
);


