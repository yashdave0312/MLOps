from pydantic import BaseModel , Field
from typing import Optional

class Employee(BaseModel):
    id : int
    name : str = Field(...,min_length = 3,max_length = 50,description = "Employee name")
    department : Optional[str] = "General"
    salary : float = Field(...,ge = 10000)

inp = {"id": 101, "name": "Yash Dave", "salary": 15000}
emp = Employee(**inp)
print(emp)