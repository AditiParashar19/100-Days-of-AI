# feedback -> analyze sentiment -> positive-> reply
#if negative -> reply according to it

# feedback -> model -> pos -> model -> response if neg -> model -> response
# only one path execute

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda #lambda to runnable
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

#model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", #"TinyLlama/TinyLlama-1.1B-Chat-v1.0",  #model 
    task="text-generation" #task to perform
)

model = ChatHuggingFace(llm=llm)

parser =StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template =" classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

result = classifier_chain.invoke({
    'feedback':'This is a terrible smart phone'
})
# print(result)
# print(result.sentiment)

prompt2 =PromptTemplate(
    template ="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 =PromptTemplate(
    template ="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

#branching
branch_chain = RunnableBranch(
    (lambda x : x.sentiment=="positive",prompt2 | model |parser),  #multiple tuples (condition,chain) or default chain
    (lambda x: x.sentiment=="negative",prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain

res = chain.invoke({
    'feedback':'This is a terrible phone'
})

print(res)

chain.get_graph().print_ascii()
