from flask import Flask, request
from flask_restful import Resource, Api

from decoder import decode
from encoder import encode

app = Flask(__name__)
api = Api(app)


class Encode(Resource):
    def post(self):
        if request.method == 'POST':
            sentence = request.get_json()['sentence']
            return encode(sentence)


class Decode(Resource):
    def post(self):
        if request.method == 'POST':
            sentence = request.get_json()['sentence']
            return decode(sentence)


api.add_resource(Encode, '/v1/encode')
api.add_resource(Decode, '/v1/decode')

if __name__ == '__main__':
    app.run(debug=True)
