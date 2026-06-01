from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()


def ingest_pdf_to_mongodb(pdf_path):
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split Documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(documents)

    # Embeddings Model
    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # MongoDB Connection
    client = MongoClient(
        "mongodb+srv://admin:admin@project.zionpmi.mongodb.net/?appName=Project"
    )

    db = client["skills"]
    collection = db["tirth"]

    # Generate Embeddings & Store
    for doc in docs:
        document_data = {
            "content": doc.page_content,
            "embedding": embeddings.embed_query(doc.page_content)
        }
        collection.insert_one(document_data)

    print(f"{len(docs)} chunks stored successfully.")


# Function Call
ingest_pdf_to_mongodb("3skills.pdf")

