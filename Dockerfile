FROM python:3.11-alpine
RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
USER nonroot
WORKDIR /app
COPY app.py .
COPY src/templates ./src/templates
RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev,test && \
    pip install -r requirements.txt
CMD ["uvicorn", "--workers", "4", "app:asgi_app", "--host", "0.0.0.0", "--port", "80"]
