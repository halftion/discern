import pymysql

def cveItemInsert(db,cve):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # SQL 插入语句：
        string = "INSERT INTO cve_info(cve_id,cve_url,cwe_id, exp, vulnerability_type, score, gainedaccess_level, access, complexity, authentication, confidentiality, integrity, availability, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = [cve['cve_id'], cve['cve_url'], cve['cwe_id'], cve['exp'], cve['vulnerability_type'], cve['score'], cve['gainedaccess_level'], cve['access'], cve['complexity'], cve['authentication'], cve['confidentiality'], cve['integrity'], cve['availability'], cve['description']]
        cursor.execute(string,value)
        db.commit()
    except Exception as e:
        print(e)

def cveProductIneset(db,item):
    cursor = db.cursor()
    try:
        # SQL 插入语句：
        string = "INSERT INTO cve_product(cve_id,product_type,vendor,product,version,updates,edition,languages) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
        value = [item['cve_id'],item['product_type'],item['vendor'],item['product'],item['version'],item['update'],item['edition'],item['language']]
        cursor.execute(string, value)
        db.commit()
    except Exception as e:
        print(e)

def cveProduct(db,info):
    cursor = db.cursor()
    list = []
    try:
        if info['vendor'] != '':
            if info['product'] != '':
                if info['version'] != '':
                    # SQL 查询语句：
                    string = "SELECT distinct cve_id FROM `product` WHERE vendor like %s and product like %s and version like %s"
                    vendor = '%' + info['vendor'] + '%'
                    product = '%' + info['product'] + '%'
                    version = '%' + info['version'] + '%'
                    value = [vendor,product, version]
                    cursor.execute(string, value)
                    results = cursor.fetchall()
                    for result in results:
                        res = {}
                        res['cve_id'] = result[0]
                        res['vendor'] = info['vendor']
                        res['product'] = info['product']
                        res['version'] = info['version']
                        list.append(res)
                    return list
                else:
                    string = "SELECT distinct cve_id FROM `product` WHERE vendor like %s and product like %s"
                    value = ['%' + info['vendor'] + '%', '%' + info['product'] + '%']
                    cursor.execute(string, value)
                    results = cursor.fetchall()
                    for result in results:
                        res = {}
                        res['cve_id'] = result[1]
                        res['vendor'] = info['vendor']
                        res['product'] = info['product']
                        res['version'] = info['version']
                        list.append(res)
                    return list
        return list
    except Exception as e:
        print(e)

def cveDetail(db,cvelist):
    cursor = db.cursor()
    detaillist = []
    if len(cvelist) > 0:
        try:
            for cve in cvelist:
                string = "SELECT * FROM `cve_info` WHERE cve_id = %s"
                value = [cve]
                cursor.execute(string, value)
                results = cursor.fetchall()
                for res in results:
                    detail = {
                        "cve_id":res[2],
                        "cve_url":res[1],
                        "cwe_id":res[3],
                        "exp":res[4],
                        "vulneravility_type":res[5],
                        "score":res[6],
                        'gainedaccess_level':res[7],
                        'access':res[8],
                        'complexity':res[9],
                        'authentication':res[10],
                        'confidentiality':res[11],
                        'integrity':res[12],
                        'availability':res[13],
                        'description':res[14]
                    }
                    detaillist.append(detail)
        except Exception as e:
            print(e)
    return detaillist


if __name__=="__main__":
    item={
        'vendor': 'Cisco',
        'product': 'IOS',
        'version':'12.',
    }
    db = pymysql.connect(host, username, passwd, dbname)
    list = ["CVE-2019-16725","CVE-2019-17319"]
    res = cveDetail(db,list)
    for r in res:
        print(r)
    db.close()