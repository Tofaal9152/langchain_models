# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableSequence

# load_dotenv()

# model = ChatOpenAI(model="gpt-4o-mini")

# prompt = PromptTemplate(template="what is a {topic}", input_variables=["topic"])

# parser = StrOutputParser()

# chain = RunnableSequence(prompt | model | parser)

# result = chain.invoke({"topic": "DOG in one line"})

# print(result)

# ✅ Recommended:
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate(template="what is a {topic}", input_variables=["topic"])

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "DOG in one line"})

print(result)
# print(type(chain)) # <class 'langchain_core.runnables.base.RunnableSequence'>
