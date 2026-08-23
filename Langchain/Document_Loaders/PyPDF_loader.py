from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
loader = PyPDFLoader("C:\Langchain-CampusX\Minor Project 1.pdf")
docs=loader.load()
print(docs)
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)