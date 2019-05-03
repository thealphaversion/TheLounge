from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send
# from forms import AccessForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

# @app.route("/home", methods=['GET','POST'])
@app.route("/")
@app.route("/home")
def home():
	# accessForm = AccessForm()
	# return render_template("home.html", form=accessForm)
	return render_template("home.html")

@app.route("/chatroom")
def chatroom():
	# nickname = request.form['Nickname']
	# return render_template("chatroom.html", name = nickname)
	return render_template("chatroom.html")

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
	# socketio.run(app, host="0.0.0.0")
	socketio.run(app)