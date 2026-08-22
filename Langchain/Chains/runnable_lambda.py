#---------------------------------------------------------------------------------------------------------------------------------------
# Demo
#----------------------------------------------------------------------------------------------------------------------------------------
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnableSequence

# def word_counter(text):
#     return len(text.split())

# #convert into runnable
# runnable_word_counter = RunnableLambda(word_counter)

# res = runnable_word_counter.invoke("Hi i am aditi")
# print(res)

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnablePassthrough,RunnableSequence
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def word_count(text):
    return len(text.split())
parser = StrOutputParser()
model =  ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt1,model,parser)
parallel_chain = RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'word_count':RunnableLambda(word_count)  #lambda x :len(x.split())
    }
)

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
res = final_chain.invoke({'topic':'AI'})
print(res)

print("="*150)
print("Joke: ",res["joke"])
print("="*150)
print("Count: ",res["word_count"])