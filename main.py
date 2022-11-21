import os
import logging
import json
import temper
from flask import Flask, jsonify
from flask_restx import Api, Resource

logging.basicConfig(level=logging.ERROR)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
api = Api(app)

nstemper = api.namespace('temper', 'Temper APIs')

@nstemper.route('/get_data')
class GetDataClass(Resource):
  def get(self):
    data = temper.get_data()
    return jsonify(data)

@nstemper.route('/get_temp')
class GetTempClass(Resource):
  def get(self):
    data = temper.get_data()
    return data["internal_temperature"]

if __name__ == '__main__':
  app.run()
