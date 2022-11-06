from com.connectMysql import Dbconnect
'''链接数据库'''
class GetData():
    def __init__(self):
        self.con = Dbconnect()

    def getUser(self,sql):
        res = self.con.select(sql)
        namelist = []
        # lenth = len(res)
        '''提取列表数据'''
        for i in range(len(res)):
            # print(res[i][0])
            namelist.append(res[i][1])
        print(namelist)
        return res

if __name__ == '__main__':
    data = GetData()
    sql = "select * from pms_users limit 2"
    data.getUser(sql)



