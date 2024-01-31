import nltk
from langchain.text_splitter import NLTKTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.vectorstores import Chroma


def save_pdf():
    loader = PyPDFLoader("document/tsd.pdf")
    documents = loader.load_and_split(text_splitter=NLTKTextSplitter())

    print("Split into %d documents" % len(documents))
    embedder = SpacyEmbeddings()
    chroma = Chroma(persist_directory="./chroma_db")
    chroma.from_documents(documents, embedder)

if __name__ == "__main__":
    nltk.download("punkt")
    save_pdf()
