import geoip2.database


reader = geoip2.database.Reader('./GeoLite2-City.mmdb')


def getPosition(ip):
    position = {}
    try:
        res = reader.city(ip)
        position['ip'] = ip
        position['city'] = res.city.name
        position['province'] = res.subdivisions.most_specific.names['zh-CN']
        position['country'] = res.country.names['zh-CN']
        position['continent'] = res.continent.names['zh-CN']
        position['countryid'] = res.country.geoname_id
        #经纬度
        position['location'] = [res.location.longitude,res.location.latitude]
    except Exception as e:
        print(e)
    return position

def getPositionlist(iplist):
    positionlist = []
    for ip in iplist:
        position = getPosition(ip)
        positionlist.append(position)
    return positionlist

def productsAppendPosition(productlist):
    newlist = []
    for product in productlist:
        position = getPosition(product['ip'])
        product['position'] = position
        newlist.append(product)
    return newlist

def countryCount(positionlist):
    list = []
    for position in positionlist:
        for item in list:
            if item['countryid'] == position['countryid']:
                item['count'] += 1
                break
            if item == list[-1]:
                data = {
                    'country':position['country'],
                    'count':1,
                    'countryid':position['countryid'],
                }
                list.append(data)
    return list



if __name__=="__main__":
    iplist = [
        '115.89.233.131',
        '115.89.233.132',
        '115.89.233.133',
        '115.89.233.134',
        '115.89.233.135',
        '115.89.233.136',
    ]
    poslist = getPositionlist(iplist)
    for pos in poslist:
        print(pos)