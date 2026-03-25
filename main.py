from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import router
import os

from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Heart Disease ML API")

# Security: Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup static files for CSS/Assets
BASE_DIR = Path(__file__).resolve().parent
app.mount("/css", StaticFiles(directory=str(BASE_DIR / "css")), name="css")

from fastapi.responses import FileResponse
from pathlib import Path

# Absolute path to the index.html at the root
BASE_DIR = Path(__file__).resolve().parent

@app.get("/")
async def read_root():
    index_path = BASE_DIR / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    return {"status": "Heart Disease ML API is live", "info": "index.html not found at root"}

@app.get("/api")
async def api_root():
    return {"message": "Heart Disease ML API Root", "version": "v1"}

app.include_router(router, prefix="/api/v1")

# Removed Jinja2 and static mounts for Vercel 
# Vercel handles the root index.html and /public assets automatically

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
