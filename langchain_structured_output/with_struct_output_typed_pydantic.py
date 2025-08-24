from model_config import model
from typing import Literal, Optional
from pydantic import BaseModel, Field


# schema
class Review(BaseModel):
    summery: str = Field(description="single sentenc about the given context")
    sentiment: Literal["poitive", "negative"] = Field(
        description="Only positive or negative in reposnse"
    )
    name: Optional[str] = Field(default=None, description="Name of the reviewer")


structured_model = model.with_structured_output(Review)


response = structured_model.invoke(
    """The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this"""
)
print(response)
