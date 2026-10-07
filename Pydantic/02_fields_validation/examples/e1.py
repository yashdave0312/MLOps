from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id : int
    items : List[str]
    quantities : Dict[str,int]

class BlogPost(BaseModel):
    title : str
    content : str
    image_url : Optional[str] =None

inp_data01 = {"user_id": 107,"items":["Laptops","Mobiles"],"quantities": {"Laptops":2,"Mobiles":3}}

cart = Cart(**inp_data01)
print(cart)