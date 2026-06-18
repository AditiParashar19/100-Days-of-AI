from google import genai
from dotenv import load_dotenv
import os

load_dotenv() # load environment variable- This reads the .env file and loads its contents into the program.

# genai.Client -> Creates a connection to Gemini using your API key.
client  = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

  #"Explain AI in simple terms"
# sends your prompt to Gemini and asks it to generate a response.

while(True):
    prompt = input("Prompt: ") 
    if(prompt.lower()=="exit"):
        print("Bye!!")
        break
    response = client.models.generate_content( 
        model = "gemini-2.5-flash",
        contents = prompt
    )
    print(response.text)