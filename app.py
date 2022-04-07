# Imports

from flask import Flask, redirect

app = Flask(__name__)

# Routes

from routes import api

app.register_blueprint(api, url_prefix='/api/')

@app.route('/')
def index():
    return redirect('/api/')

if __name__ == '__main__':
    app.run(debug=False)