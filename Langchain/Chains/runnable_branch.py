from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableBranch,RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

parser = StrOutputParser()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)
prompt2  =PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=['text']
)
def word_count(text):
    return len(text.split()) >300

#Making chains

report_gen_chain = RunnableSequence(prompt1,model,parser)

word_count_runnable = RunnableLambda(word_count)

branch_chain = RunnableBranch(
    (word_count_runnable,RunnableSequence(prompt2,model,parser)),# (condition,runnable)  lambda x:len(x.split())>500 x is whole report which we getting from parser
    RunnablePassthrough()  #input as it go forward
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)
result = final_chain.invoke({'topic':'Dolphin'})

print(result)