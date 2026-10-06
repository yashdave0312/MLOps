from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool

input_value = {
    "id": 101,
    "name":"Laptop",
    "price":12000.98,
    "in_stock":True
}    

product = Product(**input_value)
print(product)