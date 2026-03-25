import joblib
import os
from functools import lru_cache

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

@lru_cache(maxsize=1)
def get_model():
    return joblib.load(os.path.join(BASE_DIR, "models/KNN_heart.pkl"))

@lru_cache(maxsize=1)
def get_scaler():
    return joblib.load(os.path.join(BASE_DIR, "models/scaler_heart.pkl"))

@lru_cache(maxsize=1)
def get_columns():
    return joblib.load(os.path.join(BASE_DIR, "models/columns.pkl"))

# Eager load during module import
model = get_model()
scaler = get_scaler()
columns = get_columns()
