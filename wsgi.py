from flask import Flask, render_template
import ssl
import requests
import json

app = Flask(__name__)
app.Debug = True

@app.route('/')
def hello_world():
    data = requests.get('https://api.github.com/repos/origami7/gitpets').json()
    user_data = requests.get('https://api.github.com/users/origami7').json()
    print data['name']
    return render_template('index.html', picture=user_data['avatar_url'])

if __name__ == '__main__':
    app.run()
