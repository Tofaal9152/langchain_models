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


multiply = multiply_tool()

print(multiply.invoke({"a": 4, "b": "23"}))
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())
