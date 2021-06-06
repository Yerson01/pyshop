FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache gcc musl-dev python3-dev \
    libffi-dev openssl-dev cargo jpeg-dev musl-dev

COPY Pipfile .
RUN pip3 install --upgrade pip && \
    pip3 install pipenv
RUN pipenv install --system --dev --skip-lock

RUN mkdir app
WORKDIR app
COPY . /app

RUN adduser -D user
RUN chmod +rwx /app/db.sqlite3
USER user
