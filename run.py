import pytest
import os

# 运行测试报告
if __name__ == '__main__':
    # 1、查找所有测试报告用例并执行
    pytest.main(["-s",
                 "--alluredir=report/allure_report","--clean-alluredir"])
    # 2、把测试报告生成html（第一种方式）  serve启动
    # os.system(r"allure serve ./allure_raw")
    # 3、把测试报告生成html   generate生成报告    clean删除报告
    os.system("allure generate report/allure_report -o report/report_html --clean")

