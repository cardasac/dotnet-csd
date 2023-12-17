FROM python:3.11-alpine AS base

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

FROM base AS serve

COPY app.py .
COPY src ./src
COPY static ./static

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
USER nonroot

HEALTHCHECK --interval=10m --timeout=5s \
    CMD curl -f http://localhost/ || exit 1

EXPOSE 80
CMD ["gunicorn", "--bind", ":80", "--workers", "3", "--threads", "2", "--preload", "app:create_app()"]
