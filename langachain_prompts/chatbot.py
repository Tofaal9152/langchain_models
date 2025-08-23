from model_config import model

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