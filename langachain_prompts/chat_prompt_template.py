from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
# Not working
# from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} expert."),
        ("human", "Explain this {item} ino ne sentence."),
    ]
)

chain = chat_template | model

res = chain.invoke({"domain": "fruit specialist", "item": "apple"})
print(res.content)
