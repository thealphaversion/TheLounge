# TheLounge
The Lounge is a Python project for my university course project.
Here I tried playing with sockets using the flask-SocketIO library.

The web application is built using the Flask framework. This framework was chosen because flask is designed to make getting started quick and easy, with the ability to scale up when necessary. This made perfect sense at the moment because of the limited timeline of this project.
The flask framework supports the entire web app by routing us to different web pages and within this framework the flask-SocketIO library is used to create socket connections.
On the front end side, some Javascript code handles listening for, displaying and sending the messages. This javascript code is part of the SocketIO library, specifically the socket.on() method, which listens for events and handles them accordingly. On the backend side, under the socketio.on route, the handling of the events is done.
