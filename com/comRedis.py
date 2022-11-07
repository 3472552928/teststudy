import redis
from com.redTxtconfig import getini

def cofDedis():
    ip = getini(name="\conf\data.ini",section="REDIS",option="ip")
    port = getini(name="\conf\data.ini",section="REDIS",option="port")
    db = getini(name="\conf\data.ini",section="REDIS",option="db")


    pool = redis.ConnectionPool(host = ip,port=port,decode_responses=True,db = db)
    r =redis.Redis(connection_pool=pool)
    return r
    # string类型


if __name__ == '__main__':
    r = cofDedis()
    name = r.get('name')
    print(name)
    # hash类型
    h_name = r.hget('hashString','name')
    h_age = r.hget('hashString','age')
    print(h_name)
    print(h_age)
    # list类型
    list_v = r.lrange('list',0,-1)
    print(list_v)
    # set类型
    set = r.smembers('sets')
    print(set)
    # zset类型
    zset = r.zscore('sets1','12')
    print(zset)