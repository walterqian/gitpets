from flask import Flask, render_template
import ssl
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = requests.get('https://api.github.com/repos/origami7/gitpets').json()
    print data['name']
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
