from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import SessionLocal, AppV2Data, init_db

app = FastAPI()

# Initialize DB
init_db()

@app.delete("/delete/{item_id}")
async def delete_entry(item_id: int):
    db = SessionLocal()
    entry = db.query(AppV2Data).filter(AppV2Data.id == item_id).first()

    if not entry:
        db.close()
        return JSONResponse({"message": "Entry not found"}, status_code=404)

    db.delete(entry)
    db.commit()
    db.close()

    return JSONResponse({"message": f"Entry {item_id} deleted successfully"})
