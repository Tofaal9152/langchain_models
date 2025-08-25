from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableParallel


load_dotenv()
llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")

model1 = ChatOpenAI(model="gpt-4o-mini")
model2 = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate 2 merits about this {content}",
    input_variables=["content"],
)
prompt2 = PromptTemplate(
    template="Generate 2 demerits about this {content}",
    input_variables=["content"],
)
prompt3 = PromptTemplate(
    template="Generate a 2 line about this is merits {merits_output} and demerits {demerits_output}. is this good or bad?",
    input_variables=["result_output"],
)

parallel_chain = RunnableParallel(
    {
        "merits_output": prompt1 | model1 | parser,
        "demerits_output": prompt2 | model2 | parser,
    }
)
print("parallel_chain", parallel_chain)
merge_chain = parallel_chain | prompt3 | model1 | parser
print("merge_chain", merge_chain)

merge_chain.get_graph().print_ascii()

result = merge_chain.invoke({"content": "cigerate"})
print("result", result)
