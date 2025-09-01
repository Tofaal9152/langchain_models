from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory=r"Rag\retriever\vector_store_retriever\chroma_db",
    collection_name="first",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 1})

query = "Dhoni?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"result no: {i+1}")
    print("result:", doc)


# get_first_data = vector_store.get(ids=id)
# search = vector_store.similarity_search(
#     query="kera chennai ar player",
#     k=1
# )
