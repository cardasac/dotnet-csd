FROM python:3.11-alpine AS base

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS serve

COPY app.py .
COPY src/templates ./src/templates
COPY static .

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
USER nonroot

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "--threads", "2", "--preload", "app:create_app()"]
