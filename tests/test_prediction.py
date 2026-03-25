from app.services.prediction_service import predict_heart

def test_prediction():
    sample = {
        "age": 50,
        "trestbps": 120,
        "chol": 200
    }

    result = predict_heart(sample)
    assert result is not None
