from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from dotenv import load_dotenv

load_dotenv()

# HF
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model = ChatHuggingFace(llm=llm)


# # GPT
# model = ChatOpenAI(model="gpt-4o-mini")
# parser = JsonOutputParser()
# Schema
schema = [
    ResponseSchema(name="name", description="description in one line"),
    ResponseSchema(name="color", description="color of this"),
]
parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template="Write a topic on {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)
# prompt1 = template1.format(topic="apple")

# result_content = model.invoke(prompt1)
# print(result_content)
# result = parser.parse(result_content.content)
print(template1)
chain = template1 | model | parser
result = chain.invoke({"topic": "apple"})
print(result)
