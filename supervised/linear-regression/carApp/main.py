from fastapi import FastAPI
import uvicorn
from utils.responses import root_message, success_message, error_message
from schema.input import Input
from models.model import predict_price, MODEL_VERSION

app = FastAPI(description="API for car prediction")


@app.get("/")
def home_route():
    return root_message()


@app.post("/predict")
def predict(input_data: Input):
    try:
        predicted_price = predict_price(input_data)
        return success_message(price=round(predicted_price, 2), model_version=MODEL_VERSION)
    except Exception as err:
        return error_message(err)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
