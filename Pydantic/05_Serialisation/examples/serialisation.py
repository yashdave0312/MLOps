from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    zipcode : str

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool = True
    createdAt : datetime
    address : Address
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


# create an instance of the User model

user = User(
    id = 1,
    name = "Yash",
    email = "yash@example.com",
    is_active = True,
    createdAt = datetime(2024, 3, 15, 14, 30),
    address = Address(
        street = "Chhipwad",
        city = "Valsad",
        zipcode = "396001"
    ),
    tags = ["developer", "python", "pydantic"]
)    

# print(user)


# Using model_dump() to serialize the model instance to a dictionary

python_dict = user.model_dump()
print(python_dict)
print("\n")
print("=========================================\n")

# Using model_dump_json() to serialize the model instance to a JSON string

json_str = user.model_dump_json()
print(json_str)