from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", #"TinyLlama/TinyLlama-1.1B-Chat-v1.0",  #model 
    task="text-generation" #task to perform
)

model = ChatHuggingFace(llm=llm)

#create a pydantic object that acts as a schema

class Person(BaseModel):
    name : str = Field(description="name of the person")
    age:int = Field(gt=18,description="Age of the person")
    city:str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name , age and city of a fictional  {place} person\n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({
    'place':'India'
})
print(prompt)
res = model.invoke(prompt)
finalres = parser.parse(res.content)
