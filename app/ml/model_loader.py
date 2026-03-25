import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "models/KNN_heart.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models/scaler_heart.pkl"))
columns = joblib.load(os.path.join(BASE_DIR, "models/columns.pkl"))
