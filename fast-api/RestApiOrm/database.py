import os
from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy.orm import *

load_dotenv() # load environment variables from .env file

DB_USER=os.getenv("db_user")
DB_PASSWORD=os.getenv("db_password")    
DB_HOST=os.getenv("db_host")
DB_PORT=os.getenv("db_port")
DB_NAME=os.getenv("db_name")

# print(DB_NAME)

DATABASE_URI=F"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine=create_engine(DATABASE_URI)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
