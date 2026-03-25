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

# Robust Path Resolution
BASE_DIR = Path(__file__).resolve().parent

# Mount CSS for styling
css_path = BASE_DIR / "css"
if css_path.exists():
    app.mount("/css", StaticFiles(directory=str(css_path)), name="css")

# Serve UI at Root
@app.get("/")
async def read_root():
    index_path = BASE_DIR / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    return {
        "status": "Heart Disease ML API is live", 
        "info": "Frontend index.html not found",
        "debug_path": str(index_path)
    }

# API Health
@app.get("/api/health")
async def health():
    return {"status": "healthy"}

# Standardized API Routes
# This makes it respond to /api/predict
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
