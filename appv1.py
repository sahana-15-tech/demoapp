from fastapi import FastAPI
import mysql.connector
from datetime import datetime
from pydantic import BaseModel
import random

app = FastAPI()

# MySQL connection function
def get_db_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root123",
        database="demo_db"
    )
    return conn

# Define input model
class Item(BaseModel):
    random_str: str

# POST endpoint to add entry
@app.post("/add_entry/")
async def add_entry(random_str: str = None):
    db = SessionLocal()

    # Generate random number/string if none provided
    if not random_str:
        random_str = str(random.randint(1, 1000))  # random number as string

    new_entry = AppV2Data(add_date=datetime.now(), random_str=random_str)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    db.close()

    return JSONResponse({"message": "Entry added successfully", "id": new_entry.id, "random_str": random_str})
