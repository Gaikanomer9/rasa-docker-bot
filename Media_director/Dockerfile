FROM python:3.6

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r app/requirements.txt

WORKDIR /app

EXPOSE 8080

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8080", "--module", "main:app", "--processes", "2", "--threads", "3"]
