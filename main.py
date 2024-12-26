from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import List
from joblib import load

app = FastAPI()
model_path = 'artifacts/model.pkl'
print("loading model...")
model = load(model_path)
print("loaded model...")

class RegressionInputs(BaseModel):
    inputs: List[List[float]]

@app.post("/predict_value/",
             summary="api v1",
             description="api endpoint for regression")
def predict_diabete_score(unseen_data: RegressionInputs): 
     global model
     if model is None:
         model = load(model_path)
     inputs = unseen_data.inputs
     y_pred = model.predict(inputs)
     y_pred = y_pred.flatten().tolist()
     return {"predicted" : y_pred}

