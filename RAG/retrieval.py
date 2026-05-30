from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import ChatOpenAI

import os
load_dotenv()

client = MongoClient("mongodb+srv://admin:admin@project.zionpmi.mongodb.net/?appName=Project")

db = client["AdaniRAG"]
collection = db["CSE"]

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

vector_store = MongoDBAtlasVectorSearch(
    collection= collection,
    embedding=embeddings,
    index_name = "rag_index"
)

query = "what are the key skills mentione in the cv?"

ans = vector_store.similarity_search(query=query,k=3)

print("top 3 relevant documents:")

print(ans)

context = " ".join(
    doc.page_content for doc in ans
)

prompt = f"""
Answer only based on the following context.

if answer is not found in the context , say you donot know.

Contevt :{context}
Question:{query}
"""

llm = ChatOpenAI(
    model="gpt-3.5-turbo"
)

response = llm.invoke(prompt)

print(response.content)