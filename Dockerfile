FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /currency_code/requirements.txt
RUN pip install -r /currency_code/requirements.txt

COPY . /currency_code/
WORKDIR /currency_code/

EXPOSE 8000
