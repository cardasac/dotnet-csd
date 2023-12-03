FROM python:3.11-alpine AS base

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

FROM base AS serve

COPY app.py .
COPY src/templates ./src/templates

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
USER nonroot

CMD ["uvicorn", "app:ASGI", "--host", "0.0.0.0", "--port", "80"]
