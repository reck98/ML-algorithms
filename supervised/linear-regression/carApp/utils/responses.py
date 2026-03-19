from fastapi.responses import JSONResponse


def root_message():
    return JSONResponse(status_code=200, content={"message": "Hello from api server"})


def success_message(price: float, model_version: str = None):
    return JSONResponse(
        status_code=200,
        content={"message": "Success", "price": price, "model_version": model_version},
    )


def error_message(err: Exception):
    return JSONResponse(
        status_code=500, content={"message": "Internal Server Error", "error": str(err)}
    )
