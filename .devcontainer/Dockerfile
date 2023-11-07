FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system packages required by Wagtail and Django.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements needed to run testapp
COPY testapp/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp