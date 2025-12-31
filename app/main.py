from fastapi import FastAPI,HTTPException,Query
from services.products import get_products
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/products")
def products(name:str = Query(
    default="none",
    max_length=50,
    min_length=4,
    description="Search by product name",
    )):

    products = get_products()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name","").lower()]
        print(products)
    return products