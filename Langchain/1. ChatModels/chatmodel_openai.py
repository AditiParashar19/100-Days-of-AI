from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=1.2,max_completion_tokens=)
  #temperature is creativity parameter (it controls the creativity or randomness of output) 1.5 -random
# output me kitne token chaiye max_completion_tokens
result = model.invoke("What is the capital of India")
print(result.content)