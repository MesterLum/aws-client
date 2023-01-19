FROM python:3.12-alpine3.17 as base

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV TZ UTC

FROM base as builder

ENV PIPENV_VENV_IN_PROJECT 1

COPY Pipfile
COPY Pipfile.lock

RUN pipenv install --deploy

FROM base as runtime
COPY -from=builder/.venv/ .venv/

ENV PATH=".venv/bin:$PATH"


