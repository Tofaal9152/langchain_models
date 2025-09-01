from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("Rag\document_loader\sample.pdf")
docs = loader.load()


text_splitter = CharacterTextSplitter(
    chunk_size=10,
    # length_function=len,
    chunk_overlap=0,
    separator=''
)

chunks = text_splitter.split_documents(docs)

print(chunks[0])
