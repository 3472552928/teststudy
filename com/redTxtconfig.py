import os
import configparser
import yaml
import csv
cf = configparser.ConfigParser()

# 获取当前路径
# os.path.abspath(__file__)
# path = os.path.abspath(__file__)
# path1 = os.path.realpath(__file__)
#
# # 获取上一层目录
# os.path.dirname(__file__)
# path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)
# print(path1)
# print(path2)
# print(os.getcwd())
# filepath = os.path.dirname(os.getcwd())+"\conf\data.txt"
# # print(filepath)
# # print(filepath+"\conf\data.txt")
# # with open(filepath,'r') as f:
# #     print(f.readline())
#

def getTxt(name="\conf\data.txt"):
    filepath = os.path.dirname(os.path.dirname(os.path.abspath  (__file__))) + name
    with open(filepath, 'r') as f:
        res = f.readlines()
    return res
# print(getTxt())

# names = getTxt()
# print("列表里的值:{}".format(names))
# for i in names:
#     print(i)


def getini(name,section,option):
    filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + name
    cf.read(filepath)
    res = cf[section][option]
    # print(res)
    return res


getini(name="\conf\data.ini",section="HOST",option="host")



def getYaml(file):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + file
    f = open(path,"r")
    cf = f.read()
    res = yaml.safe_load(cf)
    # print(res)
    return res


# path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+ "\conf\db.yaml"
# print(path)


res = getYaml(file="\conf\db.yaml")
# print(res["login"])





# file = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# path = os.path.join(file, "conf", "usr.csv")
# # print(path)
# with open(path,"r") as f:
#     data = csv.reader(f)
#     # print(data)
#     for i in data:
#         print(i)
#     '''去第几行数据'''
    # res1= list(data)
    # print(res1[2])