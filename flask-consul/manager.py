#!/usr/bin/env python3
from flask import Flask
from views import login, blackbox, consul

app = Flask(__name__)
app.register_blueprint(login.blueprint)
app.register_blueprint(blackbox.blueprint)
app.register_blueprint(consul.blueprint)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2026)
