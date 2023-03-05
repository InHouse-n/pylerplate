#syntax=docker/dockerfile:1

FROM python:3
WORKDIR /app
COPY . .
RUN pip install "poetry==1.3.2"
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry run main