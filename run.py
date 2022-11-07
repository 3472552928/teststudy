import pytest
import os

# 运行测试报告
if __name__ == '__main__':
    pytest.main(["-sq",
                 "--alluredir","./allure_raw"])
    os.system(r"allure serve ./allure_raw")
