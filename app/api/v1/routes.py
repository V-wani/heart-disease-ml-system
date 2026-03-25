from fastapi import APIRouter
from app.api.v1.schemas import HeartInput
from app.services.prediction_service import predict_heart

router = APIRouter()

@router.post("/predict")
def predict(data: HeartInput):
    result = predict_heart(data.dict())
    return {"prediction": result}
