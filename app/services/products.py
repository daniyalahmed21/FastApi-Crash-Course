import json

def get_products():
    print("Fetching products from JSON file")
    with open("./data/products.json") as f:
        products = json.load(f)
    return products
    