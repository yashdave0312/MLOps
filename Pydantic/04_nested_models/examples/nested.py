from typing import List,Optional
from pydantic import BaseModel, Field



# Using one class as a field in another class is called nesting. This is useful for creating complex data models.

class Address(BaseModel):
    street : str
    city : str
    postal_code : str

class User(BaseModel):
    user_id : int
    name : str
    address : Address

address_data = {"street" : "Shubham Society","city" : "Valsad","postal_code" : "396001"}

add = Address(**address_data)
print(add)

User_data = {"user_id" : 1,"name" : "Yash Dave","address" : address_data}
user = User(**User_data)
print(user)


class Comment(BaseModel):
    id : int
    content : str
    # Forward reference to the Comment class itself to allow for nested comments
    replies : Optional[List["Comment"]] = None  

Comment.model_rebuild()   

comment = Comment(
    id=1,
    content="First Comment",
    replies = [
        Comment(id=2, content="reply1"),
        Comment(id=3, content="reply2")
    ]
)

print(comment)