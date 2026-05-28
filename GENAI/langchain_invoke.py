from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

import os

load_dotenv()

topic = input("enter your topic:")
marks = input("enter marks:")
difficulty = input("enter difficulty:")


client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages(
    {
        ("system","you are a helpful assistant."),
        ("user","create a question paper on topic {topic}, of marks {marks} and difficulty level {difficulty}")
    }
)

chain = prompt | client
response = chain.invoke(
    {
        "topic": topic ,
        "marks": marks,
        "difficulty": difficulty
    }
)
print(response.content)