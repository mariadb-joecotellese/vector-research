import sys

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores.pgvector import PGVector


def query_vectors(query: str):
    embedder = OllamaEmbeddings(model="llama2")
    db = PGVector(
        connection_string="postgresql+psycopg2://root:root@localhost:5432/doc_database",
        collection_name="my_docs",
        embedding_function=embedder)
    docs = db.similarity_search(query)
    if not docs:
        return "No documents found"
    return docs


def query_llm(query: str, docs: list):
    if not docs:
        return "No documents found"
    llm = Ollama(model="llama2")

    chat = query + " " + " ".join([doc.page_content for doc in docs])
    results = llm.invoke(chat)
    return results


if __name__ == "__main__":
    docs = query_vectors(sys.argv[1])
    if docs is not None:
        print(docs)
        chat = query_llm(sys.argv[1], docs)
        print(chat)