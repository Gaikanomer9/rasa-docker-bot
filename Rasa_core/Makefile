run:
	make action&
	make run-http

train-nlu:
	python -m rasa_nlu.train -c nlu_model_config.yml --fixed_model_name current \
	       --data ./data/nlu.md --path models/ --project nlu

train-core:
	python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --epochs 300

run-cmdline:
	python -m rasa_core.run -d models/dialogue -u models/nlu/current --endpoints endpoints.yml

run-http:
	python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/current -o out.log --endpoints endpoints.yml

learn:
	make train-nlu
	make train-core
	make action&
	python -m rasa_core.train --online -d models/dialogue/domain.yml -u models/nlu/current --out dialogue -s data/stories.md

action:
	python -m rasa_core_sdk.endpoint --actions actions


