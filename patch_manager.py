from flask import Flask,jsonify
import sys
from pb3 import  ProtocBaseReply

app = Flask(__name__)

@app.route("/")
def hello():
    print(sys.path)
    return "hello"

@app.route("/index")
def index():
	return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/hellojson')
def hellojson():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)


@app.route('/share/getPatch')
def hellopb():
    reply = ProtocBaseReply.BaseReply()
    reply.Code = 20000
    reply.Message = "xxxx"
    data = {'update':1,'version':'','patchUrl':'http://www.baidu.com'}
    reply.SpareParameterEntry = data
    return "hellopb"



if __name__ == "__main__":
	app.run(debug=True)
