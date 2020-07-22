from flask import *

from sys import *
from subprocess import call

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def change_music():
	ip = request.remote_addr

	if request.form['submit'] == 'spotify':
		call(["systemctl stop plexamp.service"])
		call(["systemctl start raspotify.service"])
		return render_template('success.html')
	elif request.form['submit'] == 'plex':
		call(["systemctl stop raspotify.service"])
		call(["systemctl start plexamp.service"])
		return render_template('success.html')
	else:
		return render_template('404.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

if __name__ == '__main__':
	#app.debug = True
	app.run(host='0.0.0.0', port=1025, debug=False)







