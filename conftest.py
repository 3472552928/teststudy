from api.home.login import Opmslogin
import pytest
import requests
from com.connectMysql import Dbconnect
@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    Opmslogin(s).login()
    return s




@pytest.fixture(scope="function")
def clear_data_fix():
    # 前置清理
    print("开始清理数据。。。。。")
    sql = "DELETE FROM pms_projects where aliasname = \"测试1\""
    Dbconnect().delete(sql)
    print("前置数据清理完毕。。。")
    yield
    # # 后置操作 再次清除
    Dbconnect().delete(sql)
    print("后置数据清理完毕。。。")




