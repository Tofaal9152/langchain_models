from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class multiply_schema(BaseModel):
    a: float = Field(description="First number (required)")
    b: float = Field(description="Second number (required)")


class multiply_tool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two number"
    args_schema: Type[BaseModel] = multiply_schema

    def _run(self, a: float, b: float) -> float:
        return a * b


class add_tool(BaseTool):
    name: str = "addition"
    description: str = "add two numbers"
    args_schema: Type[BaseModel] = multiply_schema

    def _run(self, a: float, b: float) -> float:
        return a + b


class MathToolkit:
    def get_tools(self):
        return [add_tool(), multiply_tool()]


toolkit = MathToolkit()
tools = toolkit.get_tools()

multiply = tools[1]
print(multiply.invoke({"a": 4, "b": "23"}))
