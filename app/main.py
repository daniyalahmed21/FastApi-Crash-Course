from fastapi import FastAPI
from services.products import get_products
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
def products():
    products = get_products()
    return products

