from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Teacher:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print(f"Teaching {self.subject}")


# Objects
student1 = Student("Aditi", 20)
student2 = Student("Rahul", 21)

teacher = Teacher("Python")

student1.display()
student2.display()
teacher.teach()

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(chunks)
print(len(chunks))
print(chunks[1])