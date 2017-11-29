import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, jsonify, Response, request, render_template
from admin import config

#解决找不到api module 问题
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(__name__)
app.config.from_object(config)


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index2")
def index2():
    return render_template('test.html')


if __name__ == "__main__":
	app.run(debug=True)
