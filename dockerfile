FROM python:3.10.11

WORKDIR /code

# Copy requirements and environment files
COPY ./requirements.txt /code/requirements.txt
COPY .env /code/.env
COPY credentials.json /code/credentials.json
COPY serviceAccount.json /code/serviceAccount.json
COPY token.json /code/token.json

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN ls
# Copy application code (including the utils directory)
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
