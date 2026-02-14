import os
from typing import Optional

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_openai.chat_models import ChatOpenAI

# Loading .env environment variables
load_dotenv()

# Models
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")
OPENAI_CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL")

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Source data path
PDF_PATH = os.getenv("PDF_PATH")

# Database configuration
PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")

def get_embeddings():
    return OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)

def get_vector_store(embeddings):
    return PGVector(
        embeddings=embeddings,
        collection_name=PG_VECTOR_COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )

def get_chat_model(model: Optional[str] = OPENAI_CHAT_MODEL):
    return ChatOpenAI(model=model)
