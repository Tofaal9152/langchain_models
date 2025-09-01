from langchain_core.tools import BaseTool, tool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini")


class multiply_schema(BaseModel):
    a: float = Field(description="First number (required)")
    b: float = Field(description="Second number (required)")


class multiply_tool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two number"
    args_schema: Type[BaseModel] = multiply_schema

    def _run(self, a: float, b: float) -> float:
        return a * b


multiply = multiply_tool()


llm_with_tools = llm.bind_tools([multiply])

result = llm_with_tools.invoke("multiply of 2 and 3")


print(multiply.invoke(result.tool_calls[0]))
