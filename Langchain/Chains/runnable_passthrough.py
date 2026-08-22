from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

passthrough = RunnablePassthrough()
print(passthrough.invoke(2))   #input -> output

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="explain the following joke = {text}",
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

res = final_chain.invoke({
    'topic':'cricket'
    })

print(res)

print("="*70)
print("Joke: ",res["joke"])

print("="*70)
print("Explanation: ",res['explanation'])