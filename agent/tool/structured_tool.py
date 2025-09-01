from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from typing import Optional


class multiply_schema(BaseModel):
    a: float = Field(..., description="First number (required)")
    b: float = Field(3, description="Second number (optional, defaults to 3)")


def multiply_fun(a, b):
    return a * b


multiply = StructuredTool(
    name="multiply",
    description="muultipy two function",
    args_schema=multiply_schema,
    func=multiply_fun,
)
print(multiply.invoke({"a": 4, "b": 23}))
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())
