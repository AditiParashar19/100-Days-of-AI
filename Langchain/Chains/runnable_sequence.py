from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 =PromptTemplate(
    template="Write  a joke about {topic}",
    input_variables=['input']
)

prompt2 = PromptTemplate(
    template="Write a description of joke = {joke}"
)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

res = chain.invoke({
    "topic":"AI"
})

print(res)
