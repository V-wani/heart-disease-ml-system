from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import router
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

# API Routes only
@app.get("/")
async def read_root():
    return {"status": "Heart Disease ML API is live", "documentation": "/api/v1/docs"}

@app.get("/api")
async def api_root():
    return {"message": "Heart Disease ML API Root", "version": "v1"}

app.include_router(router, prefix="/api/v1")

# Removed Jinja2 and static mounts for Vercel 
# Vercel handles the root index.html and /public assets automatically

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
