from pydantic import BaseModel

from typing import Dict, Any

class HeartInput(BaseModel):
    # Base clinical features
    Age: int
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    MaxHR: int
    Oldpeak: float
    # Catch-all for dynamic one-hot fields
    class Config:
        extra = "allow"
