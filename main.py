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

# Standardized API Routes matching /api/predict in Vercel
# The router defines /predict, so prefix /api makes it /api/predict
app.include_router(router, prefix="/api")

# Minimal health check for Vercel
@app.get("/api/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
