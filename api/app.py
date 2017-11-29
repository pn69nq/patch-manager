import os
import sys

from flask import Flask, jsonify, Response

#解决找不到api module 问题
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.pb3 import ProtocBaseReply
from common.util import Md5Util
from api import config

app = Flask(__name__)
app.config.from_object(config)

@app.route("/")
def hello():
    print(sys.path)
    print(os.path.dirname(__file__))
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
    return jsonify(t)\

@app.route('/md5file')
def md5file():
    md5file = os.path.dirname(__file__)+'/patch_signed_7zip.apk'
    return Md5Util.CalcFileMD5(md5file)


@app.route('/share/getPatch',methods=['post'])
def getPatch():
    reply = ProtocBaseReply.BaseReply()
    reply.Code = 20000
    reply.Message = "补丁"

    data0 = ProtocBaseReply.BaseReply.SpareParameterEntry()
    data0.key = 'update'
    data0.value = "1"
    data1 = ProtocBaseReply.BaseReply.SpareParameterEntry()
    data1.key = 'version'
    data1.value = '11111'
    data2 = ProtocBaseReply.BaseReply.SpareParameterEntry()
    data2.key = 'patchUrl'
    data2.value = 'http://www.baidu.com'

    reply.spareParameter.append(data0)
    reply.spareParameter.append(data1)
    reply.spareParameter.append(data2)
    print(reply)
    return Response(reply.encode_to_bytes(), status=200, mimetype='application/x-protobuf')


if __name__ == "__main__":
	app.run(debug=True)
