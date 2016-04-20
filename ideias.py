'''
flask
javascript
html
css


banco de dados: mysql

'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return u'Olá mundo! Elisa'

if __name__ == "__main__":
    app.run()