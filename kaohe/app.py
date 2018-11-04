from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///.\demo.db"

if __name__ == '__main__':
    app.run(debug=True)
