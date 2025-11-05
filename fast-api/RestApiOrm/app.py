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


