# # OpenAI
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from model_config import model
# load_dotenv()

# model = ChatOpenAI(model="gpt-3.5-turbo",temperature=1.5,max_completion_tokens=20)

response = model.invoke("explain gpt-5-nano pricing in one sentece")
print(response)
print("------------------")
print(response.content)
# Note: If temperature = 0, then the output is the same; if it is higher, the output may vary.