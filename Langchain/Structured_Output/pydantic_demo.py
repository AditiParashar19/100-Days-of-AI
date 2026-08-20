from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str = "aditi"   #default value
    age : Optional[int] =None
    email:EmailStr
    cgpa:float = Field(gt=0,lt=10,default=9,description="A decimal value representing the cgpa of the student")  # contraint

new_student = {'age':90,'email':'aditi','cgpa':90}   #{'name':"Aditi"} # if we pass a number then it will throw error at runtime
student =Student(**new_student)
print(student)
student_dict = dict(student)
print(type(student))
print(student_dict["age"])
print(student.name)

student_json = student.model_dump_json()

print(student_json)