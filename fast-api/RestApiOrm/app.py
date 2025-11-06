# connect to database with SQLAlchemy
from sqlalchemy import *
from fastapi import *
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

DB_USER=os.getenv("db_user")
DB_PASSWORD=os.getenv("db_password")    
DB_HOST=os.getenv("db_host")
DB_PORT=os.getenv("db_port")
DB_NAME=os.getenv("db_name")
app = FastAPI(title="CRUD APPLICATION")
# print(DB_NAME)

DATABASE_URI=F"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine=create_engine(DATABASE_URI)

@app.get("/")
def root():
    return {"message": "Welcome to the CRUD Application"}

@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT NOW()"))
            return{"status":f"connected{result.fetchall()}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
