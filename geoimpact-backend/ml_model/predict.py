import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_oil = joblib.load(os.path.join(BASE_DIR, "oil_model.pkl"))
model_stock = joblib.load(os.path.join(BASE_DIR, "stock_model.pkl"))

def predict_market(sentiment, impact, oil_prev, stock_prev):
    X = np.array([[sentiment, impact, oil_prev, stock_prev]])

    oil_pred = model_oil.predict(X)[0]
    stock_pred = model_stock.predict(X)[0]

    return oil_pred, stock_pred