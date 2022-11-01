from com.redTxtconfig import getYaml
import pymysql





class Dbconnect():
    def __init__(self,database="aiopms"):
        db = getYaml(file="\conf\db.yaml")
        ip = db["dbip"]
        port = db["port"]
        usr = db["usr"]
        pwd = db["pwd"]
        self.db = pymysql.connect(host=ip,port=port,user=usr,password=str(pwd),database=database)
        self.cursor = self.db.cursor()

    '''关闭游标'''
    def close(self):
        self.db.close()

    '''查询数据'''
    def select(self,sql):
        # sql = "select * from pms_users limit 2"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        self.db.close()
        return res


    '''修改数据'''
    def updata(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    '''删除数据'''
    def delete(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    '''插入数据'''
    def into(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()



if __name__ == '__main__':
    dc = Dbconnect()
    sql = "select * from pms_users limit 2"
    dc.select(sql)
    # sql = "UPDATE pms_users set username = \"test001\" where username = \"test1\""
    # dc.updata(sql)
    # sql = "DELETE pma_users from pms_users where username = \"test001\""
    # dc.delete(sql)
