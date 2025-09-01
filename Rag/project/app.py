from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)

load_dotenv()

# model & embeddings
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
# parser
parser = StrOutputParser()

# # document loader
# loader = TextLoader(file_path=r"transcript.txt")
# docs = loader.load()

# Texts = docs[0].page_content

# # Text splitting
# splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# chunked_docs = splitter.split_documents([docs[0]])

# Vector Store
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory=r"Rag\\project\\db",
    collection_name="chatbot",
)

# retriever
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# prompt
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are a helpful assistant.
    Answer the question based on the context: {context}.
    question: {question}
    """,
)


# utility function to format context
def format_context(retrieved_docs):
    formatted = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return formatted


# augmentations with Runnable
augmentation_chain = RunnableParallel(
    {
        "question": RunnablePassthrough(),
        "context": retriever | RunnableLambda(format_context),
    }
)
print("Augmentation Chain:", augmentation_chain)
chain = augmentation_chain | prompt | llm | parser

result = chain.invoke(
    "Does this context mention 'president'? If so, what is it? if not what is the context?"
)

print("Final Answer: ", result)
