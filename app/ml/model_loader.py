import joblib
import os
from pathlib import Path
from functools import lru_cache

# Vercel-compatible absolute path resolution
# __file__ is /var/task/app/ml/model_loader.py
# .parents[2] is /var/task/
BASE_DIR = Path(__file__).resolve().parents[2]

@lru_cache(maxsize=1)
def get_model():
    model_path = BASE_DIR / "models" / "KNN_heart.pkl"
    return joblib.load(str(model_path))

@lru_cache(maxsize=1)
def get_scaler():
    scaler_path = BASE_DIR / "models" / "scaler_heart.pkl"
    return joblib.load(str(scaler_path))

@lru_cache(maxsize=1)
def get_columns():
    columns_path = BASE_DIR / "models" / "columns.pkl"
    return joblib.load(str(columns_path))

# Load artifacts
try:
    model = get_model()
    scaler = get_scaler()
    columns = get_columns()
except Exception as e:
    print(f"CRITICAL Error loading ML artifacts: {e}")
    # Fallbacks or empty objects to prevent total app failure during import
    model = None
    scaler = None
    columns = []
