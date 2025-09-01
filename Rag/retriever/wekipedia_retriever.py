from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=1, lang="en")


query = "the geopolitical history of Bangladesh and pakistan from the perspective of a India"

docs = retriever.invoke(query)


for i, doc in enumerate(docs):
    print(f"--result: {i+1} --\n")
    print(doc)
