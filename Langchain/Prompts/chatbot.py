from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history = [
        SystemMessage(content = "You are a helpful AI assistant")
]
st.header("ChatBot")
user_input = st.text_input('You: ')
#while(True):
if(st.button("Send") and user_input ):
    
        chat_history.append(HumanMessage(content = user_input))
    # if(user_input=="exit"):
    #     break
        result = model.invoke(chat_history) #invoke function isn  flexible enough we can send list of messages also
        chat_history.append(AIMessage(content=result.content))
        st.write("AI: ",result.content)

print(chat_history)