from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# loading documents
loader = CSVLoader("document_loader\\all_solved_problems.csv")
docs = loader.load()
# docs_page_ontents = docs[0].page_content
# docs_page_metadata = docs[0].metadata
# for i in docs:
print(docs[30])
# # call model
# model = ChatOpenAI(model="gpt-4o-mini")
# # promot
# prompt = PromptTemplate(
#     template="write a summery from this topic in one line {topic}",
#     input_variables=["topic"],
# )
# # parser
# parser = StrOutputParser()
# # chain
# chain = prompt | model | parser
# # result

# result = chain.invoke({"topic": docs_page_ontents})


# print(result)
# page_content='Serial: 1
# Problem Category: brute force, implementation, math
# Problem Link: 2070/problem/B
# Rating: 1100
# Submission Date: 03.08.2025' metadata={'source': 'document_loader\\all_solved_problems.csv', 'row': 0}