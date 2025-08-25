from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel
from typing import Literal


load_dotenv()
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

model1 = ChatOpenAI(model="gpt-4o-mini")
model2 = ChatHuggingFace(llm=llm)


class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        "Give the sentiment from the content"
    )


parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Sentiment)

prompt1 = PromptTemplate(
    template="{content} \n {format_instruction}",
    input_variables=["content"],
    partial_variables={"format_instruction": parser2.get_format_instructions()},
)
sentimental_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template="write a positive feedback about this {feedback}",
    input_variables=["feedback","bal"],
)
prompt3 = PromptTemplate(
    template="write a negative feedback about this {feedback}",
    input_variables=["feedback","bal"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model1 | parser1),
    (lambda x: x.sentiment == "negative", prompt3 | model1 | parser1),
    (RunnableLambda(lambda x: "Could not process")),
)
chain = sentimental_chain | branch_chain
chain.get_graph().print_ascii()
print(chain.invoke({"content": "This phone is  good display working fine"}))
