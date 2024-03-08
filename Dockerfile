# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#RUN pip install --upgrade cffi==1.14.0
#RUN pip3 install pyopenssl
RUN apt-get update
RUN apt-get install -y build-essential cmake zlib1g-dev libcppunit-dev git subversion wget && rm -rf /var/lib/apt/lists/*
RUN wget https://www.openssl.org/source/openssl-1.0.2g.tar.gz -O - | tar -xz WORKDIR /openssl-1.0.2g
RUN ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl && make && make install
EXPOSE 5000
COPY . .
HEALTHCHECK NONE
CMD ["flask", "run"]

