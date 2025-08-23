from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

documents = [
    "apple is red and it looks like a cherry.",
    "banana is yellow and it is a tropical fruit.",
    "grape is purple and it is small and round."
]

query = "A red fruit"
query_embedding=  embeddings.embed_query(query)
doc_embeddings = embeddings.embed_documents(documents)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

index , score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(documents[index])
print("similarity score is ",score)




# Note: Cos(0) = 1, so if the cosine similarity between two vectors is high, the similarity is good.