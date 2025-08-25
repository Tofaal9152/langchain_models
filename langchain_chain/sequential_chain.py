from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List


load_dotenv()
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

model1 = ChatOpenAI(model="gpt-4o-mini")
model2 = ChatHuggingFace(llm=llm)


# prompt schema
class fact(BaseModel):
    facts: List[str] = Field(
        description="Lists of string start with numbers. like: 1.fact"
    )


parser = PydanticOutputParser(pydantic_object=fact)
parser2 = StrOutputParser()
prompt1 = PromptTemplate(
    template="Generate 5 interesting fact about this {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)
prompt2 = PromptTemplate(
    template="Generate a {method} from this {facts}",
    input_variables=["method", "facts"],
)

chain = (
    prompt1
    | model1
    | parser
    | (lambda x: {"facts": x, "method": "1 line summery"})
    | prompt2
    | model2
    | parser2
)

print(chain.invoke({"topic": "RTX 4060"}))
# chain.get_graph().print_ascii()
