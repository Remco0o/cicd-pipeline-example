#-----------------------------------------------------------

import os
import sys
import uvicorn

#-----------------------------------------------------------

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

#-----------------------------------------------------------

# Ensure the src directory is on sys.path so we can import sibling packages
CURRENT_DIR = os.path.dirname(__file__)

SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

if SRC_DIR not in sys.path:

    sys.path.insert(0, SRC_DIR)

#-----------------------------------------------------------

from calc.calculator import Calculator

#-----------------------------------------------------------

app = FastAPI(
    title="Calculator API",
    description="Arithmetic operations served via FastAPI",
    version="1.0.0",
    docs_url="/",
)

#-----------------------------------------------------------

_calculator = Calculator()

#-----------------------------------------------------------

def _ok(result):

    return JSONResponse(status_code=200, content={"result": result})

#-----------------------------------------------------------

def _error(message: str):

    return JSONResponse(status_code=500, content={"error": message})

#-----------------------------------------------------------

@app.exception_handler(RequestValidationError)
async def _validation_exception_handler(request, exc):
    
    # Convert validation errors (e.g., wrong types) into required error format
    return _error("Invalid input")

#-----------------------------------------------------------

@app.get("/sum")
async def sum_endpoint(a: float, b: float):
    try:
        return _ok(_calculator.sum(a, b))
    except Exception as e:
        return _error(str(e))

#-----------------------------------------------------------

@app.get("/difference")
async def difference_endpoint(a: float, b: float):
    try:
        return _ok(_calculator.difference(a, b))
    except Exception as e:
        return _error(str(e))

#-----------------------------------------------------------

@app.get("/product")
async def product_endpoint(a: float, b: float):
    try:
        return _ok(_calculator.product(a, b))
    except Exception as e:
        return _error(str(e))

#-----------------------------------------------------------

@app.get("/quotient")
async def quotient_endpoint(a: float, b: float):
    try:
        return _ok(_calculator.quotient(a, b))
    except Exception as e:
        return _error(str(e))

#-----------------------------------------------------------

@app.get("/square-root")
async def square_root_endpoint(x: float):
    try:
        return _ok(_calculator.square_root(x))
    except Exception as e:
        return _error(str(e))

#-----------------------------------------------------------

if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8888)

#-----------------------------------------------------------