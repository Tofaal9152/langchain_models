from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain import hub
from langchain.tools import tool
import requests
import os

weather_api_key = os.environ.get("WEATHER_API_KEY")

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")

# tools
duckduckgo_search = DuckDuckGoSearchRun()

@tool(description="Get the current weather in a given city")
def weather_tools(city: str):
    url = f"https://api.weatherstack.com/current?access_key={weather_api_key}&query={city}"
    res = requests.get(url)
    return res.json()


prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm, tools=[duckduckgo_search, weather_tools], prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[duckduckgo_search, weather_tools],
    verbose=True,
)

result = agent_executor.invoke({"input": "weather in Bangladesh"})

print(result)
