from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
chat_history = [
    SystemMessage(content="You are a mathematician who answers with a one-word result.")
]
while True:
    user_input =input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input=="exit":
        break
    res = model.invoke(chat_history)
    print("AI: ",res.content)
    chat_history.append(AIMessage(content=res.content))
    
print(chat_history)