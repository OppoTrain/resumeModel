from app import create_app
import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(create_app(), host="0.0.0.0", port=int(os.getenv("PORT", 8000)))