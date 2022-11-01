import logging
import time
import os




class Loger(object):
    '''
    封装后的logging
    '''
    def __init__(self,logger=None):
        """指定保存日志文件路径，日志级别，以及调用方法
        将日志存入到指定文件中
        """

        # 创建一个logger
        global setLev
        self.logger = logging.getLogger(logger)
        from  com.redTxtconfig import getini
        level = getini(name="\conf\data.ini",section="log",option="level")
        if level =="debug" or level == "DEBUG":
            setLev = logging.DEBUG
        elif level =="INFO" or level == "info":
            setLev = logging.INFO
        elif level =="WARN" or level == "warn" or level == "WARNING" or level == "warning":
            setLev = logging.WARN
        elif level =="ERROR" or level == "error":
            setLev = logging.ERROR
        self.logger.setLevel(setLev)

        # 创建一个handler 用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        # print(self.log_time)
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print(self.path)
        self.log_path = os.path.join(self.path,'logs')
        # print(self.log_path)
        # self.log_name = self.log_path + self.log_time + "test.log"
        self.log_name = self.log_path + "\\" + "opms_" + self.log_time + ".log"
        # print(self.log_name)

        # 创建一个handler 用于写入日志文件
        fh = logging.FileHandler(self.log_name,'a',encoding='utf-8')
        fh.setLevel(setLev)

        # 再创建一个handler用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(setLev)


        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] %(filename)s-->%(funcName)s line: %(lineno)d [%(levelname)s]-->%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        fh.close()
        ch.close()


    def getlog(self):
        return self.logger



if __name__ == '__main__':
    log = Loger().getlog()
    res1 = {"code":1,"messge":"贺喜您，登录成功"}
    log.info(res1)
    res2 = {"code":0,"messge":"登录失败"}
    if res2['code'] == 0:
        log.error("登录失败了")

