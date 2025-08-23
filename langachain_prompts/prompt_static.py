from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# Static prompt

template = PromptTemplate(
    validate_template=True,
    input_variables=["food_name", "language_name", "length"],
    template="""
You are a helpful assistant that provides information about food.

Food Name: {food_name} 
Explanation Language: {language_name}  
Explanation Length: {length}  

Please include the following details:
1. The color of the food  
2. The origin of the food  
""",
)

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
