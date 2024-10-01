FROM python:3.10-slim

RUN pip install --no-cache-dir "poetry==1.8.3"

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false 

RUN poetry install

COPY . /app


EXPOSE 8080

CMD ["fastapi", "run", "src/presentation/main.py", "--port", "8080"]
