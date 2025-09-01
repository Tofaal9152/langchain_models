from langchain_core.tools import tool


@tool(description="Multiply two numbers a and b and return the result.")
def multiply(a: float, b: float):
    return a * b


print(multiply.invoke({"a": 4, "b": 2}))
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())
