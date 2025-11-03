from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
from pathlib import Path

app = FastAPI(title="Salary Prediction API", version="0.1")

MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "model.pkl"

if not MODEL_PATH.exists():
    raise RuntimeError(f"Model not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

if not MODEL_PATH.exists():
    raise RuntimeError(f"Model not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

# --- 2. Define request & response schemas ---
class SalaryRequest(BaseModel):
    years_experience: float

class SalaryResponse(BaseModel):
    predicted_salary: float

# --- 3. Define endpoints ---
@app.get("/health")
def health():
    """Check service health."""
    return {"status": "ok"}

@app.post("/predict", response_model=SalaryResponse)
def predict(req: SalaryRequest):
    """Predict salary given years of experience."""
    try:
        X = np.array(req.years_experience).reshape(-1, 1)
        y_pred = model.predict(X)[0]
        return SalaryResponse(predicted_salary=float(y_pred))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
