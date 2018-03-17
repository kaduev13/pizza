FROM python:3.6.4-alpine

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
RUN apk update && apk add python3-dev build-base linux-headers pcre-dev postgresql-dev && pip3 install uwsgi

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /code
COPY . /code
COPY entrypoint.sh /

EXPOSE 8000

CMD ["/entrypoint.sh"]