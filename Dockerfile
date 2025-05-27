FROM python:3.11-alpine
LABEL maintainer="Model Context Protocol Server < Pistil Data > "

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts

EXPOSE 8000

ARG DEV=false

RUN apk add --update --no-cache \
    libffi-dev \
    rust \
    cargo \
    curl && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache \
        postgresql-client \
        jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base \
        postgresql-dev \
        musl-dev \
        zlib \
        zlib-dev \
        linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        fastapi-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/temp && \
    chown -R fastapi-user:fastapi-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER fastapi-user

CMD ["run.sh"]
