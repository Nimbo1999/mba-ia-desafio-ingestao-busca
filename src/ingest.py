from dataclasses import dataclass
from typing import Iterable, Optional

from config import (
    PDF_PATH,
    get_embeddings,
    get_vector_store,
)
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

@dataclass
class SplitterConfig:
    chunk_size: int
    chunk_overlap: int

def load_documents(path: str) -> list[Document]:
    loader = PyPDFLoader(path)
    return loader.load()

def split_documents(docs: Iterable[Document], config: Optional[SplitterConfig] = None):
    # Valores padrão se config não for fornecido
    if config is None:
        config = SplitterConfig(chunk_size=1000, chunk_overlap=150)

    # Cria o splitter com a configuração
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
    )

    return text_splitter.split_documents(documents=docs)

def ingest_pdf():
    print("Starting PDF ingestion...")
    print(f"Loading PDF from: {PDF_PATH}")
    docs = load_documents(PDF_PATH)
    documents = split_documents(docs)
    if not documents:
        raise SystemExit(0)
    
    enriched_documents = [
        Document(
            page_content=doc.page_content,
            metadata={k: v for k, v in doc.metadata.items() if v not in (None, "", [])}
        )
        for doc in documents
    ]
    ids = [f"doc-{i}" for i in range(len(enriched_documents))]

    embeddings = get_embeddings()
    store = get_vector_store(embeddings)

    results = store.add_documents(documents=enriched_documents, ids=ids)
    print(f"Ingested {len(results)} documents into the vector store.")

if __name__ == "__main__":
    ingest_pdf()
