from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.retrievers.multi_query import MultiQueryRetriever

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model="gpt-4o-mini")

vectore_store = Chroma(
    embedding_function=embeddings,
    persist_directory=r"Rag\retriever\multi_query_retriever\chroma_db",
    collection_name="multi_query",
)


multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectore_store.as_retriever(search_kwargs={"k": 5}),
    llm=llm,
)
query = "How to improve energy levels and maintain balance?"
print("multi_query_retriever")
multiquery_results = multiquery_retriever.invoke(query)

for i, doc in enumerate(multiquery_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

# retriever
retriever = vectore_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

print("retriever")
retriever = retriever.invoke(query)
for i, doc in enumerate(retriever):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

# search
search = vectore_store.similarity_search(query=query, k=5)
print("search")
for i, doc in enumerate(search):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)


# all_docs = [
#     Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
#     Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
#     Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
#     Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
#     Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
#     Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
#     Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
#     Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
#     Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
#     Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
# ]
