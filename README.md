# Vector Research

Is this a basic reasearch project to better understand vector embeddings and Retrieval Augmented Generation

The goal of this project is to use an LLM to "chat" with a PDF.

1. Extract text from PDF
2. chunk the text
3. use embeddings to vectorize the text chunks
4. store the chunks in a database
5. connect an LLM
6. run a query that will
   1. get the data from vector database
   2. pass it + query to LLM
   3. display the results

## Requirements

[Poetry](https://python-poetry.org/)
[Ollama](https://ollama.ai)
[Docker](https://www.docker.com/)

## Installation

You need to install Postgres and PGVector. There is a `docker-compose` file you can use for this.

```shell
docker-compose up -b
```
This will build and start the docker container with Postgres

Next you need to setup your python environment

```shell

poetry install
poetry shell

```

Then to load a PDF into the vector database

`python load_pdf.py FILENAME`

Then to query the PDF

`python query_pdf.py "QUERY STRING"`

