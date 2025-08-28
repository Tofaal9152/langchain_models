from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
    RunnableBranch,
)
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")


# Schema
class Review(BaseModel):
    summery: str = Field(description="short summery of the review")
    sentiment: Literal["positive", "negative"] = Field(
        "Only positive or negative in reposnse"
    )


parser = PydanticOutputParser(pydantic_object=Review)

str_parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="{topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)
prompt2 = PromptTemplate(
    template="write a 3 line summery about this {sentiment} sentiment",
    input_variables=["sentiment"],
)

generate_review_chain = prompt1 | model | parser

review_explanation_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | str_parser),
    (lambda x: x.sentiment == "negative", prompt2 | model | str_parser),
    (RunnablePassthrough()),
)
para = RunnableParallel(
    {
        "alltext": RunnablePassthrough() ,
        "answer": review_explanation_chain,
    }
)
final_chain = generate_review_chain | para

result = final_chain.invoke(
    {
        "topic": """The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this"""
    }
)

print(result)
