FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /blog_api
WORKDIR /blog_api
COPY . /blog_api/
RUN pip install -r requirements.txt