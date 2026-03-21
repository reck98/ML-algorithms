import pickle
from schema.input import Input
import pandas as pd
from pathlib import Path as FilePath

MODEL_PATH = FilePath("models/car-price-prediction-model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

MODEL_VERSION = "0.0.1"

MODEL_COLUMNS = model.feature_names_in_




def predict_price(input_data: Input) -> float:
    data = {col : 0 for col in MODEL_COLUMNS}
    
    data["year"] = input_data.year
    data["mileage"] = input_data.mileage
    data["tax"] = input_data.tax
    data["mpg"] = input_data.mpg
    data["engineSize"] = input_data.engineSize
    data["model_ " + input_data.model] = 1
    data["transmission_" + input_data.transmission] = 1
    data["fuelType_" + input_data.fuelType] = 1

    df = pd.DataFrame(data, index=[0])
    pred = model.predict(df)[0]
    # pred = max(pred, 0)
    return abs(pred)


def get_model_version() -> str:
    return MODEL_VERSION