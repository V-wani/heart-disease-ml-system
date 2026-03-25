import numpy as np
import pandas as pd
from .model_loader import scaler, columns

def preprocess(data):
    """
    Transforms raw input dictionary into a scaled numpy array aligned with the model's expected columns.
    Follows the reference logic:
    1. Create dataframe
    2. Fill missing columns with 0
    3. Reorder columns to match expected_columns
    4. Scale
    """
    # Create input dataframe
    input_df = pd.DataFrame([data])

    # Fill in missing columns with 0s
    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match the model's training requirement
    input_df = input_df[columns]

    # Scale the input
    return scaler.transform(input_df)
