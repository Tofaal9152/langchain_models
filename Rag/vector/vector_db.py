# pip install langchain chromadb openai tiktoken pypdf langchain_openai langchain-community
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="Rag\\vector\\chroma_db",
    collection_name="first",
)


# doc1 = Document(
#     page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style.",
#     metadata={"team": "Royal Challengers Bangalore", "role": "Batsman"},
# )

# doc2 = Document(
#     page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm leadership.",
#     metadata={"team": "Mumbai Indians", "role": "Batsman / Captain"},
# )

# doc3 = Document(
#     page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills and wicketkeeping are legendary.",
#     metadata={"team": "Chennai Super Kings", "role": "Wicketkeeper / Captain"},
# )

# doc4 = Document(
#     page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and pace.",
#     metadata={"team": "Mumbai Indians", "role": "Bowler"},
# )

# doc5 = Document(
#     page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding is also a highlight.",
#     metadata={"team": "Chennai Super Kings", "role": "All-rounder"},
# )


# docs = [doc1, doc2, doc3, doc4, doc5]


# POST
# vector_store.add_documents(docs)

# GET
# get = vector_store.get(include=["metadatas"])

# serching
# search = vector_store.similarity_search(
#     query="kera chennai ar player",
#     k=1
# )
# print(search)

# filtering
# filter = vector_store.similarity_search(
#     query="",
#     filter={'team': "Chennai Super Kings"}
# )
# print(filter)

# PATCH
id = "7eeb717d-2459-4f6a-824f-5ded11499044"
deleted_id= "5cbd95a9-f607-430b-a69b-f0b89ffb93ad"
data = Document(page_content="kuttar baccha fut fute sundor",metadata={"info": "updated"})

vector_store.update_document(document_id=id, document=data)
# vector_store.delete(ids=[deleted_id])

get_first_data = vector_store.get(ids=deleted_id)
print(get_first_data)


# {'ids': ['7eeb717d-2459-4f6a-824f-5ded11499044', 'f642ece5-ae03-4621-9db2-e3873b4644ba', '47a565b1-3c71-44ab-98bc-6e2fa95f777d', '7a818fa2-3856-4a71-88c7-8a36fcc39196', '5cbd95a9-f607-430b-a69b-f0b89ffb93ad'],

#  'embeddings': None, 'documents': [

#      'Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style.',

#      "Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm leadership.",

#      'MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills and wicketkeeping are legendary.',

#      'Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and pace.',

#      'Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding is also a highlight.'],

#  'uris': None,

#  'included': ['metadatas', 'documents'], 'data': None,

#  'metadatas': [
#      {'team': 'Royal Challengers Bangalore', 'role': 'Batsman'},
#      {'role': 'Batsman / Captain', 'team': 'Mumbai Indians'},
#      {'role': 'Wicketkeeper / Captain', 'team': 'Chennai Super Kings'},
#      {'team': 'Mumbai Indians', 'role': 'Bowler'},
#      {'role': 'All-rounder', 'team': 'Chennai Super Kings'}]}
