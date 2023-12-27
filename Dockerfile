FROM python:3.11-alpine AS base

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn[gthread]==21.2.0

FROM node:alpine AS static
WORKDIR /app

COPY static ./static
COPY package.json package-lock.json .
RUN npm ci && npm run build

FROM base AS serve
WORKDIR /app
COPY app.py .
COPY src ./src
COPY --from=static /app/static ./static

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
USER nonroot

HEALTHCHECK --interval=10m --timeout=5s \
    CMD curl -f http://localhost/ || exit 1

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "--threads", "8", "--preload", "app:create_app()"]
