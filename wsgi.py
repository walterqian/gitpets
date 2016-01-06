from flask import Flask, render_template
import ssl
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = requests.get('https://api.github.com/events').json()
    print data[0]['public']
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
