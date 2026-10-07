from pydantic import BaseModel
from typing import Optional,List

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

class Lesson(BaseModel):
    title : str
    duration : str

class Module(BaseModel):
    title : str
    lessons : List[Lesson]

class Course(BaseModel):
    title : str
    description : Optional[str] = "No description"
    modules : List[Module]   

Lesson_data = [
    {"title" : "Lesson 1","duration" : "10 min"},{"title" : "Lesson 2","duration" : "15 min"}    
]

module_data = [
    {"title" : "Module 1","lessons" : Lesson_data}
]   

course_data = {"title" : "Python Course","description" : "Learn Python","modules" : module_data}

course = Course(**course_data)
print(course)