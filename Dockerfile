# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev
COPY requirements.txt requirements.txt
#RUN yum -y update
#RUN yum -y install gcc
#RUN yum install gcc
RUN pip install -r requirements.txt
RUN pip install pyOpenSSL --upgrade
EXPOSE 5000
COPY . .
HEALTHCHECK NONE
CMD ["flask", "run"]

