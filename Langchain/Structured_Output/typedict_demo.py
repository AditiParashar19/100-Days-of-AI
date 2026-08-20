from typing import TypedDict

#create a definition of dictionary
class Person(TypedDict):
    name:str
    age:int 
new_person: Person={'name':'Aditi','age':76}

print(new_person)