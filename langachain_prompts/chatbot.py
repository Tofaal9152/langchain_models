from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
chat_history = []
while True:
    user_input =input("You: ")
    chat_history.append(user_input)
    
    if user_input=="exit":
        break
    res = model.invoke(chat_history)
    print("AI: ",res.content)
    chat_history.append(f"AI: {res.content}")
    
print(chat_history)