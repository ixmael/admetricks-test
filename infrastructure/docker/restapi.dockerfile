FROM python:3.10.13-alpine3.18 as pythonBase

COPY ./packages/backend /app

WORKDIR /app

RUN apk add poetry --no-cache && \
    poetry install --only main

ENTRYPOINT [ "poetry" ]
CMD [ "run", "gunicorn", "server:app" ]
