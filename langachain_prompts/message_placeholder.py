from model_config import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage


chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent from a passport office. You will chat based on previous history data."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ]
)

# load chat history
chat_history = [
    ("human", "Hello, who are you?"),
    ("assistant", "How can I help you today?"),
    ("human", "Where is my passport?"),
    ("assistant", "You will get it in 5 days."),
]


chain = chat_template | model
res = chain.invoke(
    {
        "query": HumanMessage(content="its been two days where is my passport?"),
        "chat_history": chat_history,
    }
)
print(res.content)
