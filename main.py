from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1.routes import router
from pathlib import Path
import os

app = FastAPI(title="Heart Disease ML API")

# Security: Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Absolute path resolution
BASE_DIR = Path(__file__).resolve().parent

# Mount Static Files (CSS, etc.) from the public directory
# Vercel's working directory is the root
public_dir = BASE_DIR / "public"
if public_dir.exists():
    app.mount("/css", StaticFiles(directory=str(public_dir / "css")), name="css")
    app.mount("/public", StaticFiles(directory=str(public_dir)), name="public")

# UI Root Route
@app.get("/")
async def read_root():
    index_path = public_dir / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    return {"status": "Heart Disease ML API is live", "info": "UI index.html not found in public/"}

# Health check / API Root
@app.get("/api")
async def api_root():
    return {"message": "Heart Disease ML API Root", "version": "v1"}

# API Routes
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
