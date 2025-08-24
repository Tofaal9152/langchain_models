# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

# HF
# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta", task="text-generation"
# )
# model = ChatHuggingFace(llm=llm)

# GPT
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()
# 1
template1 = PromptTemplate(
    template="Write a  topic on {topic} in one line",
    input_variables=["topic"],
)
# 2
template2 = PromptTemplate(
    template="Write a {line} line summery on the following text: {text} ",
    input_variables=["text", "line"],
)

# chain1 = template1 | model
# chain2 = template2 | model

# result1 = chain1.invoke({"topic": "Apple"})
# result2 = chain2.invoke({"text": result1.content})

# print(result2)

chain = (
    template1
    | model
    | parser
    | (lambda x: {"text": x, "line": 2})
    | template2
    | model
    | parser
)

result = chain.invoke({"topic": "Black Hole"})
print(result)
