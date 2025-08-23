# # Claude
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="anthropic-1")

response = model.invoke("What is the capital of France?")
print(response)