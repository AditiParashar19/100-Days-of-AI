from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", #"TinyLlama/TinyLlama-1.1B-Chat-v1.0",  #model 
    task="text-generation" #task to perform
)

model2 = ChatHuggingFace(llm=llm) 

prompt1= PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet":RunnableSequence(prompt1,model1,parser),
    "linkedin":RunnableSequence(prompt2,model2,parser)
})

result = parallel_chain.invoke({
    'topic':'AI'
})

print(result)
