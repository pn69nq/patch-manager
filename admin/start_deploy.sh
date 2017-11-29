#!/bin/bash
#virtualenv venv
#source venv/bin/activate
#pip install -r requirements.txt
gunicorn -w4 -b0.0.0.0:9000 app:app