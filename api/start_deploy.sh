#!/bin/bash
#virtualenv venv
#source venv/bin/activate
pip3 install -r requirements.txt
gunicorn -w4 -b0.0.0.0:5000 app:app