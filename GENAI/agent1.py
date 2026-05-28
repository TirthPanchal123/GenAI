import requests
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from dotenv import load_dotenv
import os
load_dotenv()

@tool
def get_weather(city: str):
    """Return current weather of a city."""
    
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    
    return response.json()['current_condition'][0]["FeelsLikeC"]

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key= os.getenv('OPENAI_API_KEY')
)

client_with_tools = client.bind_tools([get_weather])

response = client_with_tools.invoke(
    "what is the weather in Ahmedabad?"
)

print(response.tool_calls)

if response.tool_calls:

    tool_call = response.tool_calls[0]

    tool_arg = tool_call["args"]

    result = get_weather.invoke(tool_arg)

    print(result)

else:
    print(response.content)