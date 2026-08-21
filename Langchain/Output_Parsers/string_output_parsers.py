#from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct", #"TinyLlama/TinyLlama-1.1B-Chat-v1.0",  #model 
#     task="text-generation" #task to perform
# )

# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 1st prompt ->detailed report

template1  =PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)


#2nd prompt -> summary

template2  =PromptTemplate(
    template='write a 5 line summary on the following text.\n {text}',
    input_variables=['text']
)

prompt1  =template1.invoke({'topic':'blackhole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)

