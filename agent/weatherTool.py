from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

import os

load_dotenv()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages(
    {
        ("system","you are a helpful assistant."),
        ("user","give me weather{city}")
    }
)

chain = prompt | client
response = chain.invoke(
    {
        "city":"Ahmedabad"
    }
)
print(response.content)