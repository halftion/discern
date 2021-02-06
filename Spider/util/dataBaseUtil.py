import pymysql

host = ""
username = ""
passwd = ""
dbname = ""


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

# if __name__=="__main__":
#     item = {
#         'cve_id':"1",
#         'product_type':'',
#         'vendor':'',
#         'product':'',
#         'version':'',
#         'update':'',
#         'edition':'',
#         'language':''
#     }
#     db = pymysql.connect(host,username,passwd,dbname)
#     cveProductIneset(db,item)
#     db.close()