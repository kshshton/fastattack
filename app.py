from flask import Flask
from flask_cors import CORS

from api import data_filter

app = Flask(__name__, static_folder='./ui/dist', static_url_path='/')
cors = CORS(app, resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return '''
            Shalom, shalom!
            Cóż za slalom!
            '''
    

@app.route("/api", methods=['GET', 'OPTIONS'])
def api(url = 'https://jsonplaceholder.typicode.com/todos/'):
    return data_filter(url)


if __name__ == '__main__':
    app.run
