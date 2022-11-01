import requests
# 正则
# import re
import re
from com.geData import getHost

class OpmsAdd():
    def __init__(self,s = requests.session(), head={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}):
        self.s = s
        self.head = head
        self.host = getHost()
        # self.login_post()

        # 登录接口

    # def login_post(self,username = "libai",pwd = "csyz@1234"):
    #     #     login_url = self.host + "/login"
    #     #     datas = {"username":username,
    #     #                  "password": pwd}
    #     #     res = self.s.post(url=login_url, headers=self.head, data=datas)
    #     #
    #     #     # 正则提取text格式
    #     #     # mes = re.findall('r'"message":"(.*?)"',res.text)[0]
    #     #     # print(mes)
    #     #     print(res.text)
    #     #     return res

    # 新增接口

    def add(self,name = "测试",aliasname = "1222",started = "2022-06-21",ended= "2022-06-21", desc= "111",id = "0"):
        url = self.host + "/project/add"
        datas = {"name": name, "aliasname": aliasname, "started": started, "ended": ended, "desc": desc,
                 "id": id}
        res = self.s.post(url=url, headers=self.head, data=datas)
        print("name的值是：",name,"aliasname的值是：",aliasname)
        print(res.text)
        # return res.json()["id"]
        # print("name的值是:",name)
        return res

    # 编辑接口

    def editpro(self,id):
        url = self.host + "/project/edit/" + id
        datas = {"name": "测www试",
                 "aliasname": "1222",
                 "started": "2022-06-21",
                 "ended": "2022-06-21",
                 "desc": "1122221",
                 "projuserid": "请选择项目负责人",
                 "produserid": "请选择产品负责人",
                 "produserid": "请选择产品负责人",
                 "testuserid":"请选择测试负责人",
                 "id":id
                }
        res = self.s.post(url=url,headers=self.head,data=datas)
        print(res.text)
        return res

    # 修改状态
    def status(self,id):
        url = self.host + "/project/ajax/status" + id
        datas = {"status":"4"
            ,"id":"id"}
        res = self.s.post(url=url,headers=self.head,data=datas)
        print(res.url)

    # 文件上传
    def uploadFile(self):
        url = self.host + "/uploadmulti"
        file = {"uploadFiles":(open("D:\\R-C.jpeg","rb"))}
        res = self.s.post(url=url,files=file)
        print(res.text)

    # 新增需求添加接口·
    def addneed(self,id,filename,name="测试w",source="1",level="1",stage="1",desc=""):
        url = self.host + "/need/add/" + id
        data = {"name":name,
                "source":source,
                "level":level,
                "stage":stage,
                "acceptid":"请选择指派给",
                "tasktime":"0",
                "desc":desc,
                "acceptance":"1",
                "projectid":id,
                "id":id}
        file = {"uploadFiles":(open(filename, "rb"))}
        res = self.s.post(url=url,data=data,files=file)
        print(res.text)
        return res






if __name__ == '__main__':
    host = "http://123.56.170.43:8888"
    op = OpmsAdd()
    op.add()
    # op.uploadFile()
    # pid = op.add()
    # filename = "D:\\R-C.jpeg"
    # op.addneed(pid,filename=filename)