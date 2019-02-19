FROM quay.io/keboola/docker-custom-python:latest

COPY . /code/
WORKDIR /data/out/tables/

CMD ["python", "-u", "/code/main.py"]