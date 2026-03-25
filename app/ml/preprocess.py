import numpy as np
from .model_loader import scaler, columns

def preprocess(data):
    """
    Optimized data preprocessing for single inference.
    Uses O(N) traversal with dictionary lookups to align with model features.
    """
    # Create feature vector aligned with the trained model's expected columns
    # Efficiently handles missing features by defaulting to 0
    features = [data.get(col, 0) for col in columns]
    
    # Transform to 2D numpy array for the scaler (1, N)
    arr = np.array(features).reshape(1, -1)
    
    # Apply pre-trained scaling
    return scaler.transform(arr)
