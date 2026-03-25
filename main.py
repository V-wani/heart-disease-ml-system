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

# High-Performance API Route matching exactly what Vercel/User expects
# router has /predict, so prefix /api makes it /api/predict
app.include_router(router, prefix="/api")

# Healthcare check
@app.get("/api")
async def api_root():
    return {"message": "Heart Disease ML API Root", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
