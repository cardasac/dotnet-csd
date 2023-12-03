FROM python:3.11-alpine
COPY app.py /app
RUN pipx install poetry
COPY poetry.lock pyproject.toml /app/

WORKDIR /app
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev,test
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]