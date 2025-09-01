from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


text = """from typing import List
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain.output_parsers import (
    StructuredOutputParser,
    ResponseSchema,
    PydanticOutputParser,
)
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

# HF
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model = ChatHuggingFace(llm=llm)


# # GPT
# model = ChatOpenAI(model="gpt-4o-mini")
# parser = JsonOutputParser()
# Schema
class Company(BaseModel):
    name: str = Field(description="it must be a company name")
    products: List[str] = Field(description="product of the company")


parser = PydanticOutputParser(pydantic_object=Company)

template1 = PromptTemplate(
    template="Compnay name is {company_name} \n {format_instruction}",
    input_variables=["company_name"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)
# prompt1 = template1.format(topic="apple")

# result_content = model.invoke(prompt1)
# print(result_content)
# result = parser.parse(result_content.content)
print(template1)
chain = template1 | model | parser
result = chain.invoke({"company_name": "apple"})
print(result)
"""

text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
    # keep_separator=True
)
chunks = text_splitter.split_text(text)


print(len(chunks))

for i in chunks:
    print(f"{i}\n --------------------------------\n")
