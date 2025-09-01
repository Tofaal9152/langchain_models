from langchain.schema import Document

doc = Document(
    page_content="LangChain makes it easy to build LLM-powered applications.",
    metadata={"source": "docs/langchain", "page": 5}
)

print(doc)