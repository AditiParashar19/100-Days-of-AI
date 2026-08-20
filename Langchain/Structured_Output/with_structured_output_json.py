from langchain_google_genai  import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# schema

# Copy code
json_schema = 


structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke("The hardware is great, but the software feels bloated.There are too many pre-installed apps that I can't remove.Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this")

print(result)
print(type(result))
print("Summary: ",result.summary)
print("Sentiment: ",result.sentiment)

# when we give structure to output then a internally a prompt crated let say you are an AI assistant that extracts structured insights form text.given a product review ,extract summmary : a breif overview of the mian painnts,sentiment:overall tone of the review (positive,neg,neutral)
