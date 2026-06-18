from google  import genai
from dotenv import load_dotenv
import os

#Load environment variables
# GEMINI API KEY is store in .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if(not API_KEY):
    raise ValueError("Geminin API Key not found...")

# Create gemini client
client = genai.Client(
    api_key= API_KEY
)

# Store Chat history
history=[]  # make a list

system_prompt = """
You are a friendly AI assistant
Rules:
1. Be helpful
2. Be professional
3. Keep answers clean and concise
4. Remember previous conversation context
"""

print("="*50)

print("Welcome to Gemini Chatbot!!!")
print("="*50)
while True:
    user_input = input("Prompt: ")
    if(user_input.lower() in ["bye","exit","stop","quit"]):
        print("Bye!!")
        break
    #Store user message
    history.append(f"User : {user_input}")
    conversation_context = system_prompt +"\n"
    conversation_context+="\n".join(history)  #list converted to string

    try: 
        #Call Gemini
        response = client.models.generate_content(
            model ="gemini-2.5-flash",
            contents=conversation_context
        )
        bot_response = response.text
        print(f"\nGemini : {bot_response}")

        #Store bot response
        history.append(f"Assistant: {bot_response}")

    except Exception as e:
        print("Gemini service temporarily unavailable!!")






