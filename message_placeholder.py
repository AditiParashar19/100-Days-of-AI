from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage

#chat `template`

chat_template = ChatPromptTemplate(
    [
        ('System','You are a helpful customer support agent'),
        MessagePlaceholder(variable_name = 'chat_history'), #It has previous message context so that it understands new query
        ('human':'{query}')
    ]
)

#load the chat history
chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create prompt
prompt = chat_template.invoke({
    'chat_history':chat_history,
    'query':'where is my refund'
})

print(prompt)