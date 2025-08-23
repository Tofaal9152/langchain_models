import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables once
load_dotenv()

# Create a single model instance
model = ChatOpenAI(model="gpt-4o-mini")
