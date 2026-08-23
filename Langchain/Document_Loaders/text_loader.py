from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# create loader object
loader = TextLoader('C:\Langchain-CampusX\sample.txt',encoding='utf-8') #text filepath
docs = loader.load()  #load as a document
#loader.load() always returns a list of Document objects, even if there's only one document

model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash")
prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=['poem']
)
parser = StrOutputParser()

print(docs)
print(type(docs))
print(len(docs))
print(docs[0])
print(type(docs[0]))
print(docs[0].metadata)

chain = prompt | model | parser
final_res = chain.invoke({'poem':docs[0].page_content})
print(final_res)