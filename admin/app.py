import os
import sys

from flask import Flask, jsonify, Response, request, render_template

#解决找不到api module 问题
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
