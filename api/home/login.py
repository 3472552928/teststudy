import requests


class Opmslogin():
    def __init__(self,s = requests.session(),host="http://121.5.121.62:8088"):
        self.host=host
        self.s = s
    def login(self,username="libai",password= "csyz@1234"):
        url = self.host+"/login"
        head = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        datas = {"username": username,
                 "password": password}
        res = self.s.post(url=url,headers=head,data=datas)
        print(res.text)
        return res

    # def loginout(self):
    #     url = self.host+"/logout"
    #     res = requests.get(url=url)
    #     print(res)
    #     return res


if __name__ == '__main__':
    cl =Opmslogin()
    cl.login()