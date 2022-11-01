from api.project.add import OpmsAdd
import pytest
import os
import allure

def test_addpro_1(login_fixture,clear_data_fix):
    s = login_fixture
    OpmsAdd(s).add()


# 通过fixture进行参数化 ，一个变量多个值
# para = ['测试','别名','2022-03-01','2022-05-01','测试1']
# @pytest.fixture(params=para)
# def geetdata(request):
#     return request.param
# def test_addpro_(login_fixture,geetdata):
#     s = login_fixture
#     OpmsAdd(s).add(name=geetdata[0])



# 通过fixture进行参数化 ，多个变量多个值
# para = [['测试1','别名','2022-10-01','2022-05-01','测试1'],
#         ['测试2','别名2','2022-03-01','2022-05-01','测试1'],
#         ['测试6','别名3','2022-03-01','2022-05-01','测试3']]
#
# @allure.epic("项目名称")
# @allure.feature("项目管理")
# @allure.story("项目名称为空，添加失败")
# @allure.step("name不填,添加项目")
# @pytest.fixture(params=para)
# def getdata(request):
#     return request.param
# def test_addpro1(login_fixture,getdata,clear_data_fix):
#     s = login_fixture
#     OpmsAdd(s).add(name=getdata[0],aliasname=getdata)


@allure.epic("项目名称")
@allure.feature("项目管理")
@allure.story("添加项目：项目名称为空，添加失败")
@allure.severity("NORMAL")
@allure.step("name不填,添加项目")
def test_addpro(login_fixture,name=""):
    s = login_fixture
    ad = OpmsAdd(s)
    res = ad.add(name)
    assert res.json()['code']==0


@allure.epic("项目名称")
@allure.feature("项目管理")
@allure.story("添加项目：项目别名为空，添加失败")
@allure.severity("NORMAL")
@allure.step("aliasname不填,添加项目")
def test_addpro1(login_fixture,aliasname=""):
    s = login_fixture
    ad = OpmsAdd(s)
    res = ad.add(aliasname=aliasname)
    assert res.json()['code']==0


@allure.epic("项目名称")
@allure.feature("项目管理")
@allure.story("添加项目：项目开始日期为空，添加失败")
@allure.severity("NORMAL")
@allure.step("started不填,添加项目")
def test_addpro2(login_fixture,started=""):
    s = login_fixture
    ad = OpmsAdd(s)
    res = ad.add(started=started)
    assert res.json()['code']==0

@allure.epic("项目名称")
@allure.feature("项目管理")
@allure.story("添加项目：项目结束日期为空，添加失败")
@allure.severity("NORMAL")
@allure.step("ended不填,添加项目")
def test_addpro3(login_fixture,ended=""):
    s = login_fixture
    ad = OpmsAdd(s)
    res = ad.add(ended=ended)
    assert res.json()['code']==0


@allure.epic("项目名称")
@allure.feature("项目管理")
@allure.story("添加项目：项目备注为空，添加失败")
@allure.severity("NORMAL")
@allure.step("desc不填,添加项目")
def test_addpro4(login_fixture,desc=""):
    s = login_fixture
    ad = OpmsAdd(s)
    res = ad.add(desc=desc)
    assert res.json()['code']==0


@allure.epic("项目名称")
@allure.feature("项目管理")
@allure.story("添加项目：添加成功")
@allure.severity("CRITICAL")
@allure.step("desc不填,添加项目")
def test_addpro5(login_fixture):
    s = login_fixture
    ad = OpmsAdd(s)
    res = ad.add()
    assert res.json()['code']==1