from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# Dynamic Propmt
template = load_prompt("./prompt_template/food.json")
prompt = template.invoke(
    {"food_name": "bannana", "language_name": "english", "length": "20 words"}
)

print(prompt)
print("------------------")
result = model.invoke(prompt)
print("------------------")
print(result)
print("------------------")
print(result.content)
