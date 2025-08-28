from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt1 = PromptTemplate(template="what is a {topic}", input_variables=["topic"])
prompt2 = PromptTemplate(template="how many legs in {topic}", input_variables=["topic"])

parser = StrOutputParser()

parrarel_chain = RunnableParallel(
    {
        "first_topic": RunnableSequence(prompt1, model, parser),
        "second_topic": RunnableSequence(prompt2, model, parser),
    }
)

result = parrarel_chain.invoke({"topic": "DOG in one line"})

print(result)
# print(type(chain)) # <class 'langchain_core.runnables.base.RunnableSequence'>
