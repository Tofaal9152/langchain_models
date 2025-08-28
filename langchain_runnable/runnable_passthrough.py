from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
)

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt1 = PromptTemplate(
    template="tell me a short joke abot {joke}", input_variables=["joke"]
)
prompt2 = PromptTemplate(template="explain this {joke}", input_variables=["joke"])

parser = StrOutputParser()

gen_joke = RunnableSequence(prompt1, model, parser)

parrarel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation_joke": RunnableSequence(prompt2, model, parser),
    }
)

final_chain = RunnableSequence(gen_joke, parrarel_chain)
result = final_chain.invoke({"joke": "Dog"})

print(result)
# print(type(chain)) # <class 'langchain_core.runnables.base.RunnableSequence'>
