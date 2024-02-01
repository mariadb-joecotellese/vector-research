import sys

import nltk
from langchain.text_splitter import NLTKTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.pgvector import PGVector

CONNECTION_STRING = "postgresql+psycopg2://root:root@localhost:5432/doc_database"


def save_pdf(filename: str):
    try: 
        loader = PyPDFLoader(filename)
        documents = loader.load_and_split(text_splitter=NLTKTextSplitter())

        print("Split into %d documents" % len(documents))
        embedder = OllamaEmbeddings(model="llama2")
        PGVector.from_documents(
            embedding=embedder,
            documents=documents,
            collection_name="my_docs",
            connection_string=CONNECTION_STRING
        )
    except ValueError as e:
        print(e)
    return


if __name__ == "__main__":
    nltk.download("punkt")
    save_pdf(sys.argv[1])
