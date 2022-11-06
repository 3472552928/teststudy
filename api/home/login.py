import requests
from com.loger import Loger




class Opmslogin():
    def __init__(self,s = requests.session(),host="http://121.5.121.62:8088"):
        self.host=host
        self.s = s
        self.log = Loger().getlog()
    def login(self,username="libai",password= "csyz@1234"):
        url = self.host+"/login"
        # head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        datas = {"username": username,
                 "password": password}
        res = self.s.post(url=url,data=datas)
        '''打印日志'''
        self.log.info("data是:{}，返回是:{}".format(datas,res.text))
        '''两种方式都可以'''
        # self.log.info(res.text)
        print(res.text)
        return res

    # def loginout(self):
    #     url = self.host+"/logout"
    #     res = self.s.get(url=url)
    #     # self.log.info(res.text)
    #     print(res)
    #     return res


if __name__ == '__main__':
    cl =Opmslogin()
    cl.login()
    # cl.loginout()