from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")


messages = [
    SystemMessage(content="You are a helpful doctor."),
    HumanMessage(content="I am bleeding from my hand."),
]

res = model.invoke(messages)
messages.append(AIMessage(content=res.content))

print(messages)