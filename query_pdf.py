import sys

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores.pgvector import PGVector
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def query_vectors(query: str):
    embedder = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en-v1.5"
    )
    db = PGVector(
        connection_string="postgresql+psycopg2://root:root@localhost:5432/doc_database",
        collection_name="my_docs",
        embedding_function=embedder)
    docs = db.similarity_search_with_relevance_scores(query)
    if not docs:
        return "No documents found"
    return docs


def query_llm(query: str, docs: list):
    model = Ollama(model="llama2")
    prompt = ChatPromptTemplate.from_template("""
You are a helpful programming assistant.
You are an expert in programming
You will answer the following {query} programming question.
You will use the following documents to answer the question: {docs}
If you show code examples the should be properly formatted and indented.
""")
    output_parser = StrOutputParser()

    chain = prompt | model | output_parser
    results = chain.invoke({"query": str, 
                            "docs": docs})
    # results = ""
    return results
#

if __name__ == "__main__":
    docs = query_vectors(sys.argv[1])
    if docs is not None:
        chat = query_llm(sys.argv[1], docs)
        print(chat)