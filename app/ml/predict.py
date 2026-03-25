from .model_loader import model
from .preprocess import preprocess

def make_prediction(data):
    processed = preprocess(data)
    return model.predict(processed)[0]
