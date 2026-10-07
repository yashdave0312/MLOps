from pydantic import BaseModel, field_validator,model_validator,computed_field 


# field_validator
class User(BaseModel):
    username : str

    @field_validator('username')
    def user(cls,v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return v

inp = {"username":"Yash"}

user = User(**inp)
print(user)


# model_validator

class SignUp(BaseModel):
    passw : str
    con_pass : str

    @model_validator(mode = "after")
    def check_pass(cls,values):
        if values.passw != values.con_pass:
            raise ValueError("Password and Confirm Password must be same")
        return values

inp0 = {"passw":"Yash@123","con_pass":"Yash@123"}
sign = SignUp(**inp0)
print(sign)     


# computed_field

class Product(BaseModel):
    price : float
    quantity : int

    @computed_field
    @property
    def total(self) -> float:
        return self.price * self.quantity

inp1 = {"price":100.0,"quantity":5}
prod = Product(**inp1)
print(prod)    