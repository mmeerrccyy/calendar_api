FROM python:3.12-slim

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

RUN poetry install --no-dev

EXPOSE 80

ENV PYTHONUNBUFFERED=1

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
