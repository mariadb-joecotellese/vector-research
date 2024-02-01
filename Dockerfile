ARG PG_MAJOR=16
FROM postgres:latest
ARG PG_MAJOR

RUN apt-get update && \
		apt-mark hold locales

RUN apt-get install -y --no-install-recommends postgresql-$PG_MAJOR-pgvector
