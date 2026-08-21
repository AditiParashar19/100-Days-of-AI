#from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct", #"TinyLlama/TinyLlama-1.1B-Chat-v1.0",  #model 
#     task="text-generation" #task to perform
# )

# we can also use google gemma model

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

parser = StrOutputParser()

# we need only the result.content so parser will do that it will give use the string content that we need further 
chain = template1 | model | parser | template2 | model | parser #because we dont need meta need we need only content

result = chain.invoke({
    'topic':'black hole'
})

print(result)
