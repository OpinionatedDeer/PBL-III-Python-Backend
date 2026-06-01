import fastapi
import asyncio
import os
import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from config import SETUP

import datetime

# Local
import db
import routes.login as login
import routes.admin as admin
import routes.user as user
import routes.chats as chats 

if str(SETUP).lower()=="false":
    app = fastapi.FastAPI()
    app.add_middleware(
	    CORSMiddleware,
	    allow_origins=["*"],
	    allow_credentials=True,
	    allow_methods=["*"],
	    allow_headers=["*"]
    )
    @app.on_event("startup")
    async def startup():
        await db.init_db() 
    @app.on_event("shutdown")
    async def shutdown():
        await db.close_db()
    app.include_router(login.router)
    app.include_router(admin.router)
    app.include_router(user.router)
    app.include_router(chats.router)
    # Optional: run uvicorn if this file is executed directly
    if __name__ == "__main__":
        uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)

elif str(SETUP).lower()=="true":

else:
    print("Error in dotenv file, please fix\nby either downloading .env file from github and editing or\nseeing the fields and fixing")
    
