import sys

from langchain.text_splitter import TokenTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.pgvector import PGVector

CONNECTION_STRING = "postgresql+psycopg2://root:root@localhost:5432/doc_database"



def save_pdf(filename: str):
    try:
        loader = PyPDFLoader(filename)
        print("Loading PDF")
        documents = loader.load_and_split(text_splitter=TokenTextSplitter(
            chunk_size=1000,
            chunk_overlap=0
        ))
        print("Saving to database")
        embedder = HuggingFaceEmbeddings(
            model_name="BAAI/bge-large-en-v1.5"
        )
        PGVector.from_documents(
            embedding=embedder,
            documents=documents,
            collection_name="my_docs",
            connection_string=CONNECTION_STRING,
            pre_delete_collection=False

        )
    except ValueError as e:
        print(e)
    return


if __name__ == "__main__":
    save_pdf(sys.argv[1])
