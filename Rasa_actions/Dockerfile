FROM python:3.6

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5055

CMD python -m rasa_core_sdk.endpoint --actions actions
