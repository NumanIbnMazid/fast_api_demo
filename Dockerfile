FROM python:3.8.10

ENV DEBIAN_FRONTEND=noninteractive
ENV DOCKER_BUILDKIT=1
ENV BUILDKIT_INLINE_CACHE=1

WORKDIR /proj

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    build-essential

COPY requirements.txt /requirements/requirements.txt

RUN pip install -r /requirements/requirements.txt

COPY . /proj
