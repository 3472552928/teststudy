import pytest
import re
import allure
from api.home.login import Opmslogin
from com.redTxtconfig import getYaml

res = getYaml(file="\conf\db.yaml")
# print(res["login"])
part = res["login"]


# 参数化数据分离使用yaml封装
@pytest.mark.parametrize("username,password,code", part)
def test_login_4(username, password, code):
    res = Opmslogin().login(username=username, password=password)
    # re_code = (res.status_code)
    print(res.json()['code'])
    # assert re_code == 200

# 用户名为空
def testlogin_1():
    res = Opmslogin().login(username="")
    code = res.json()["code"]
    assert code == 0

# # 参数化用户名测试  @pytest.mark.parametrize("username",["","libai","libai123","libai "," libai"])
@pytest.mark.parametrize("username,code",[("",0),
                                           ("libai",1),
                                           ("libai123",0)])

@allure.epic("opms项目")
@allure.feature("登录模块")
@allure.story("登录测试")
@allure.step("异常场景测试")
# @allure.severity("CRITICAL")
@allure.severity("NORMAL")
def testlogin_3(username,code):
    res = Opmslogin().login(username=username)
    re_code = res.json()["code"]
    assert re_code == code

# # 密码参数化测试   re_code = (res.status_code)(断言服务器状态码)
# @pytest.mark.parametrize("username",["", "libai" , "libai123"])
# @pytest.mark.parametrize("password",["", "opms123456", "1234354"])
# def testlogin_2(username,password):
#     res = Opmslogin().login(username=username,password=password)
#     re_code = (res.status_code)
#     print(res.text)
#     assert re_code == 200


@allure.epic("opms项目")
@allure.feature("登录模块")
@allure.story("登录测试:用户名密码正确")
@allure.step("正常场景测试")
@allure.severity("CRITICAL")
def testlogin4():
    res = Opmslogin().login()
    print(res.json())
    assert res.status_code == 200
