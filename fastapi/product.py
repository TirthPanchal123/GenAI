from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


products = []



class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

@app.post("/post_products")
def add_product(product: Product):
    products.append(product.dict())
    return {
        "message": "Product added successfully",
        "data": products
    }

@app.get("/get_products")
def get_products():
     return {
        "message": "Product retrieved successfully",
        "data": products
    }


