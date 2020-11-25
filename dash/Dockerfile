FROM python:3.8

COPY . /app
WORKDIR /app
COPY requirements.txt /home/project/dash
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt


CMD ["gunicorn","-w 1", "--threads=1", "-b 0.0.0.0:8000", "app:server"]

