FROM python:3.6

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python -m rasa_nlu.train -c nlu_model_config.yml --fixed_model_name current --data ./data/nlu.md --path models/ --project nlu

RUN python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --epochs 300

EXPOSE 5005

CMD python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/current -o out.log --endpoints endpoints.yml