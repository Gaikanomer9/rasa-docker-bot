#!/bin/bash
python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/current -o out.log --endpoints endpoints.yml