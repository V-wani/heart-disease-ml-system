import pickle
import os
import joblib

BASE_DIR = os.getcwd()
file_path = os.path.join(BASE_DIR, "models", "KNN_heart.pkl")

print(f"Trying to load: {file_path}")
print(f"File size: {os.path.getsize(file_path)}")

try:
    with open(file_path, "rb") as f:
        data = pickle.load(f)
    print("Pickle load successful!")
except Exception as e:
    print(f"Pickle load failed: {e}")

try:
    data = joblib.load(file_path)
    print("Joblib load successful!")
except Exception as e:
    print(f"Joblib load failed: {e}")
