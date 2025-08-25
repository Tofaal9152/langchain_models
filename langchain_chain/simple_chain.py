from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")


# prompt schema
class fact(BaseModel):
    facts: List[str] = Field(
        description="Lists of string start with numbers. like: 1.fact"
    )


parser = PydanticOutputParser(pydantic_object=fact)

prompt = PromptTemplate(
    template="Generate 5 interesting fact about this {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = prompt | model | parser

# print(chain.invoke({"topic": "RTX 4060"}))
chain.get_graph().print_ascii()
