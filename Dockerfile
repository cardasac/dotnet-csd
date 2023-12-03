# syntax=docker/dockerfile:1
FROM python:3.11-alpine
COPY ./src /app
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app
RUN pip install Flask
EXPOSE 5000
CMD ["flask", "run"]
