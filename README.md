# Vector Research

This is a simple project to better understand vector embeddings and Retrieval Augmented Generation

The goal of this project is to use an LLM to "chat" with a PDF.
This is all running locally

1. Extract text from PDF
2. chunk the text
3. use embeddings to vectorize the text chunks
4. store the chunks in a database
5. connect an LLM
6. run a query that will
   1. get the data from vector database
   2. pass it + query to LLM
   3. display the results

In this example, The prompt is a programming assistant. I have used python documentation I've downloaded as a PDF.

You can find examples by googling "Python reference|tutorial|guide inurl:pdf"

## Requirements

[Poetry](https://python-poetry.org/)

[Ollama](https://ollama.ai)

[Docker](https://www.docker.com/)

## Installation

### Docker

You need to install Postgres and PGVector. There is a `docker-compose` file you can use for this.

```shell
docker-compose up -b
```
This will build and start the docker container with Postgres

### Python

Next you need to setup your python environment

```shell

poetry install
poetry shell

```
### Ollama

Ollama is a handy app that creates a local API to talk to models. 
Install Ollama and when prompted to install the command-line tool say Yes

Then from a bash shell

`ollama pull llama2:7b`

You can experiment with other models too.

## Usage
Then to load a PDF into the vector database

`python load_pdf.py FILENAME`

Then to query the PDF

`python query_pdf.py "QUERY STRING"`

