import os
from pathlib import Path
import joblib

print(Path(__file__).resolve().parent.parent)
MODEL_PATH = Path(__file__).resolve().parents[2] / "day_1" / "model" / "model.pkl"
print(MODEL_PATH)

model = joblib.load(MODEL_PATH)
print('done!!')
