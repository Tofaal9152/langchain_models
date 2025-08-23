from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-5-nano")

response = llm.invoke("write a 5 line poem about the sea")
print(response)