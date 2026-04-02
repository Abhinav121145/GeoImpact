import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample training data (you will replace later with real data)
data = {
    "sentiment": [-0.8, -0.5, 0.2, 0.5, 0.7],
    "impact_score": [-0.9, -0.6, 0.1, 0.6, 0.8],
    "oil_prev": [80, 82, 83, 85, 86],
    "stock_prev": [42000, 41800, 42100, 43000, 43500],
    "oil_change": [5, 3, -1, -2, -3],
    "stock_change": [-4, -2, 1, 3, 4]
}

df = pd.DataFrame(data)

X = df[["sentiment", "impact_score", "oil_prev", "stock_prev"]]

y_oil = df["oil_change"]
y_stock = df["stock_change"]

model_oil = LinearRegression()
model_stock = LinearRegression()

model_oil.fit(X, y_oil)
model_stock.fit(X, y_stock)

joblib.dump(model_oil, "oil_model.pkl")
joblib.dump(model_stock, "stock_model.pkl")

print("Models trained and saved")