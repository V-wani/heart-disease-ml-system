from sqlalchemy import Column, Integer, Float, String
from app.db.database import Base

class PredictionRecord(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    prediction = Column(Integer)
