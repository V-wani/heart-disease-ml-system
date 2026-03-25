from app.ml.predict import make_prediction

def predict_heart(data: dict):
    prediction = make_prediction(data)

    if prediction == 1:
        return "High Risk of Heart Disease"
    return "Low Risk"
