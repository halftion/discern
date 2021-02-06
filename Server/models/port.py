import pymysql
import models
import models.hostScan
import models.sqlAssist
from flask import jsonify


def getScan(req):
    data={}
    data['code'] = 500
    ip = req['ip']
    if ip != '':
        try:
            db = pymysql.connect(host, username, passwd, dbname)
            iplist = ip.split(',')
            data['data'] = models.hostScan.portlist_scan(iplist)
            db.close()
            data['code'] = 200
        except Exception as e:
            print(e)
    elif ip == '':
        data['code'] = 300
        data['data'] = []
    return jsonify(data)

def getVul(req):
    data = {}
    data['code'] = 500
    ip = req['ip']
    try:
        db = pymysql.connect(host, username, passwd, dbname)
        data['data'] = models.hostScan.vul_scan(db,ip)
        db.close()
        data['code'] = 200
    except Exception as e:
        print(e)
    return jsonify(data)

def getVulDetail(req):
    cve_list = req['cve']
    data = {}
    data['code'] = 500
    try:
        db = pymysql.connect(host, username, passwd, dbname)
        data['data'] = models.sqlAssist.cveDetail(db,cve_list)
        db.close()
        data['code'] = 200
    except Exception as e:
        print(e)
    return jsonify(data)

def getGeodata():
    data = ''
    return data

def getIotdata():
    data = ''
    return data

def getGrid():
    data = ''
    return data

def getType():
    data = ''
    return data

def getVulRatio():
    data = ''
    return data




if __name__=="__main__":
    # getScan('49.205.165.83,115.89.233.131')
    getVul('115.89.233.131')
