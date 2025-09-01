from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


vector_store = FAISS.load_local(
    r"Rag\retriever\mmr\FAISS_db",
    embeddings=embeddings,
    allow_dangerous_deserialization=True,
)


retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,
        "lambda_mult": 0.5, # (0-1) = (diversity - similerity)
    },
)

query = "What is langchain?"
results = retriever.invoke(query)
all_docs = vector_store.docstore._dict.values()
print(all_docs)
print("------------------")
for i, doc in enumerate(results, 1):
    print(f"--Result {i}--")
    print(doc)


# database content
# dict_values(
#     [
#         Document(
#             id="08fee381-15b6-411e-9678-b1652a580a74",
#             metadata={},
#             page_content="LangChain makes it easy to work with LLMs.",
#         ),
#         Document(
#             id="7e2d4b1e-52dc-4362-b596-da4ee6bc7d44",
#             metadata={},
#             page_content="LangChain is used to build LLM based applications.",
#         ),
#         Document(
#             id="0469b943-4fe5-4396-b0ac-d854cf13e11c",
#             metadata={},
#             page_content="Chroma is used to store and search document embeddings.",
#         ),
#         Document(
#             id="3b8b4c1b-8ce7-4e65-bf03-c6dbcba87730",
#             metadata={},
#             page_content="Embeddings are vector representations of text.",
#         ),
#         Document(
#             id="5e400ec3-5001-4c80-b6fa-11acf153c4ed",
#             metadata={},
#             page_content="MMR helps you get diverse results when doing similarity search.",
#         ),
#         Document(
#             id="69df2c5e-8a2e-4cd0-aef8-39a40238c747",
#             metadata={},
#             page_content="LangChain supports Chroma, FAISS, Pinecone, and more.",
#         ),
#     ]
# )
