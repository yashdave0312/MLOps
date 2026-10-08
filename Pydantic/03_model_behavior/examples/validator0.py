from pydantic import BaseModel , field_validator,model_validator,computed_field,Field
from typing import List,Optional,Literal

class Category(BaseModel): #Pydantic Model
    name: Literal['starter','main course', 'desert', 'beverage']

class Model(BaseModel):  
    id           :   int
    name         :   str             = Field(...,min_length=3,max_length=50, description="Item name", alias='ItemName') 
    price        :   float           = Field(...,gt=0,description="Item price") 
    category     :   Category        = Field(...,description="Item category")
    is_available :   bool            = Field(default=True) 
    description  :   Optional[str]   = None    

    # Field Validator to convert the name to title case
    @field_validator("name")
    def name_title(cls,v) -> str:
        return v.title()

    # FIELD_VALIDATOR CAN WORK FOR ONLY SINGLE FIELD, BUT MODEL_VALIDATOR CAN WORK FOR MULTIPLE FIELDS

    # Model Validator
    @model_validator(mode='after')
    def check_available(self):
        if self.is_available and self.price <= 0 :
            raise ValueError("Available items must have a price greater than zero.")
        return self

    # Computed Field
    @computed_field
    @property
    def price_with_tax(self) -> float:
        return self.price * 1.08  # Assuming a tax rate of 18%


item = Model(id=1,ItemName='chicken biryani',price=250.0,category = Category(name = "main course"))
print(item)    