import joblib
model = joblib.load('/content/car_pipeline')
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  pydantic import BaseModel
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods = ['*'],
    allow_headers = ['*']
)
class example (BaseModel):
  year:int
  transmission:str
  mileage:int
  fuelType:str
  tax:int
  mpg:int
  engineSize:int
  Manufacturer:str
@app.post('/predict')
def predict(data:example):
  car = pd.DataFrame([data.model_dump()])
  return {"prediction of car's price is":model.predict(car)[0]}




