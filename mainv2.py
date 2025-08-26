from appv2 import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("mainv2:app", host="0.0.0.0", port=8000, reload=True)