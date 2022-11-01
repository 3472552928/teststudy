import csv
import os


class ReadCsv():
    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.file = os.path.join(path, "conf", "usr.csv")


    def readALL(self,end,start):
        res =[]
        with open(self.file,"r") as f:
            self.data = csv.reader(f)
            for i in self.data:
                # print(i)
                res.append(i)
        print(res[start:end+1])
        return res[start:end+1]

    '''按行提取'''
    def readRow(self,i):
        with open(self.file,"r") as f:
            data = csv.reader(f)
            res = list(data)
            print(res[i])
        return res

    '''按列提取'''
    def readLine(self,i=1):
        with open(self.file,'r') as f:
            data = csv.reader(f)
            for line in data:
                print(line[0])

if __name__ == '__main__':
    cs = ReadCsv()
    data = cs.readALL(end=30,start=1)
    # print(data)
    # cs.readRow(i=2)
    # cs.readLine()




#
# file = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# path = os.path.join(file, "conf", "usr.csv")
# # print(path)
# with open(path,"r") as f:
#     data = csv.reader(f)
#     # print(data)
#     for i in data:
#         print(i)
#     '''去第几行数据'''
#     # res1= list(data)
#     # print(res1[2])