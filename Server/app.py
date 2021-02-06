from flask import Flask,request
from flask_cors import *
import models
import models.port

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/scan', methods = ['POST'])
def scan_requst():
    return models.port.getScan(request.json)

@app.route('/detail', methods = ['POST'])
def detail_requst():
    return models.port.getVul(request.json)

@app.route('/vul_detail', methods = ['POST'])
def vul_detail_requst():
    return models.port.getVulDetail(request.json)

# @app.route('/geodata', methods = ['GET'])
# def vul_detail_requst():
#     return models.port.getGeodata()
#
# @app.route('/country_iot_data', methods = ['GET'])
# def vul_detail_requst():
#     return models.port.getIotdata()
#
# @app.route('/grid_data', methods = ['GET'])
# def vul_detail_requst():
#     return models.port.getGrid()
#
# @app.route('/type_chart', methods = ['GET'])
# def vul_detail_requst():
#     return models.port.getType()
#
# @app.route('/panel', methods = ['GET'])
# def vul_detail_requst():
#     return models.port.getVulRatio()


if __name__ == '__main__':
    app.run()
