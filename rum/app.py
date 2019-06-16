import requests
import json
from flask import Flask, Response
import pysnooper


app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    r = requests.get('http://localhost:4000/request')
    return Response(r.content, content_type='application/json')


@app.route('/request', methods=['GET'])
def request():
    return Response(json.dumps({'result': 'OK'}), content_type='application/json')


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0', port=4000)
