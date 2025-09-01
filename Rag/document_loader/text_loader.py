from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# loading documents
loader = TextLoader("document_loader\sample.txt")
docs = loader.load()
docs_page_ontents = docs[0].page_content
# call model
model = ChatOpenAI(model="gpt-4o-mini")
# promot
prompt = PromptTemplate(
    template="write a summery from this topic in one line {topic}",
    input_variables=["topic"],
)
# parser
parser = StrOutputParser()
# chain
chain = prompt | model | parser
# result

result = chain.invoke({"topic": docs_page_ontents})


print(result)
