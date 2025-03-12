FROM python:3.12-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add --update \
    curl \
    && rm -rf /var/cache/apk/*d

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
