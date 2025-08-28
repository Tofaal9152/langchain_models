from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)


def CountJokeLength(sentence):
    return len(sentence.split())


load_dotenv()
parser = StrOutputParser()
model = ChatOpenAI(model="gpt-4o-mini")


prompt1 = PromptTemplate(
    template="tell me a short joke abot {joke}", input_variables=["joke"]
)
prompt2 = PromptTemplate(template="explain this {joke}", input_variables=["joke"])


gen_joke = RunnableSequence(prompt1 , model , parser)
parrarel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": RunnableLambda(CountJokeLength),
    }
)

final_chain = RunnableSequence(gen_joke, parrarel_chain)


result = final_chain.invoke({"joke": "Dog"})

print(result)
