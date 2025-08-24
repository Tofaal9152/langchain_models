from model_config import model

# JSON Schema
review_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "summery": {
            "type": "string",
            "description": "Single sentence about the given context",
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative"],
            "description": "Only positive or negative in response",
        },
        "name": {
            "type": ["string", "null"],
            "description": "Name of the reviewer (optional)",
        },
    },
    "required": ["summery", "sentiment"],
}

# Structured model with JSON schema
structured_model = model.with_structured_output(schema=review_schema)

response = structured_model.invoke(
    """The hardware is great, but the software feels bloated. 
    There are too many pre-installed apps that I can't remove. 
    Also, the UI looks outdated compared to other brands. 
    Hoping for a software update to fix this"""
)

print(response)
