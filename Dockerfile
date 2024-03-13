# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY openssl.txt openssl.txt
RUN pip install -r openssl.txt
EXPOSE 5000
COPY . .
HEALTHCHECK NONE
CMD ["flask", "run"]

