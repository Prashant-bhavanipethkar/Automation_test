from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import numpy as np

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(area: float = Form(...)):
    prediction = model.predict(np.array([[area]]))
    return {"predicted_price_lakhs": round(prediction[0], 2)}
