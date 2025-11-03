from pydantic import BaseModel

class PredictRequest(BaseModel):
    years_experience: float

class PredictResponse(BaseModel):
    predicted_salary: float
