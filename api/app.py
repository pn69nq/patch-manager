import os
import sys

from flask import Flask, jsonify, Response, request, render_template, send_from_directory

# 解决找不到api module 问题
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api.pb3 import ProtocBaseReply
from common.util import Md5Util
from api import appinit

# 初始化放在appinit 中进行
app = appinit.app_create()


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
	return jsonify(t) \
 \
 \
@app.route('/md5file')
def md5file():
	md5file = os.path.dirname(__file__) + '/patch_signed_7zip.apk'
	return Md5Util.CalcFileMD5(md5file)


# 下载补丁包格式url+/patch/patch_signed_7zip.apk
@app.route('/patch/<patch_name>', methods=['GET'])
def getApk(patch_name):
	def _f(abs_path):
		with open(abs_path, 'rb') as f:
			m = 500 * (1 << 10)
			while 1:
				chunk = f.read(m)
				yield chunk
				if not chunk:
					break

	try:
		abs_path = os.path.dirname(__file__) + '/apk_patch/' + patch_name
		mimetype = 'application/octet-stream'
		return Response(
			_f(abs_path), mimetype=mimetype,
			direct_passthrough=True)
	except IOError:
		return Response(u'文件不存在')


@app.route('/share/getPatch', methods=['post'])
def getPatch():
	# print(request.form['channel'])
	reply = ProtocBaseReply.BaseReply()
	reply.Code = 20000
	reply.Message = 'msg'

	baseUrl = '192.168.1.142:5000'
	data0 = ProtocBaseReply.BaseReply.SpareParameterEntry()
	data0.key = 'update'
	data0.value = "1"
	data1 = ProtocBaseReply.BaseReply.SpareParameterEntry()
	data1.key = 'version'
	data1.value = '11111'
	data2 = ProtocBaseReply.BaseReply.SpareParameterEntry()
	data2.key = 'patchUrl'
	data2.value = baseUrl + '/patch/patch_signed_7zip.apk'

	reply.spareParameter.append(data0)
	reply.spareParameter.append(data1)
	reply.spareParameter.append(data2)
	print(reply)
	return Response(reply.encode_to_bytes(), status=200, mimetype='application/x-protobuf')


@app.route('/uploads', methods=['post'])
def uploaded_file():
	dist_dir = os.path.dirname(__file__) + '/apk_patch/'
	submitted_file = request.files['file']
	filename = "patch_signed_7zip.apk"
	submitted_file.save(os.path.join(dist_dir, filename))
	return "ok"


if __name__ == "__main__":
	app.run(debug=True)
