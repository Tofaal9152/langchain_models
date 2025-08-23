# model_config.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables once
load_dotenv()

# Create a single model instance
model = ChatOpenAI(model="gpt-4o-mini")
