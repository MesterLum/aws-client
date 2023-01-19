FROM python:3.10-alpine3.17 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV TZ UTC

FROM base as builder

ENV PIPENV_VENV_IN_PROJECT 1

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pip --upgrade

RUN pip install pipenv

RUN pipenv install --deploy

FROM base as runtime

COPY --from=builder /.venv/ /.venv/

ENV PATH="/.venv/bin:$PATH"

WORKDIR /usr/src/backend

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
