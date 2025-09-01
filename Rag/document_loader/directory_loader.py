from langchain_community.document_loaders import DirectoryLoader,PyPDFDirectoryLoader,PyPDFLoader,TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# loading documents
loader = DirectoryLoader(path="document_loader\\books",glob="*.pdf",loader_cls=PyPDFLoader)
# loader = PyPDFDirectoryLoader(path="document_loader\\books")
# docs = loader.load()

# docs_page_contents = docs[0].page_content
# docs_page_metadata = docs[31].metadata
# print(docs)
# print(docs_page_metadata)
# print(docs)
# lazyload
docs2 = loader.lazy_load()

for i in docs2:
    print(i.metadata)