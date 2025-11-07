# connect to database with SQLAlchemy
from sqlalchemy import *
from fastapi import *
from models import *
from database import *
from sqlalchemy.orm import *

app = FastAPI(title="CRUD APPLICATION")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to the CRUD Application"}

# @app.get("/test-db")
# def test_db():
#     try:
#         with engine.connect() as connection:
#             result = connection.execute(text("SELECT NOW()"))
#             return{"status":f"connected{result.fetchall()}"}
#     except Exception as e:
#         return {"status": "error", "message": str(e)}

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("Database session error:", e)
    finally:
        db.close()