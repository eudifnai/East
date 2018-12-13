#coding:utf-8

import os

l = list()
dir = os.path.abspath(os.path.dirname(__file__))
l.append(dir)
print(dir)

class opr_txt(object):

    def __init__(self, filename):
        self.filename = dir + "/config/" + filename
        print(self.filename)

    def read_txt(self):
        """
        泛化filename最合适
        :return: 全部读取出来内容
        """
        with open(self.filename, "r", encoding="utf-8") as fb:
            res = fb.read()
            return res

    def write_txt(self, text=''):
        """
        写入并创建文件，有原文件会被覆盖
        :param text:str
        :return:结果信息
        """
        with open(self.filename, "w", encoding="utf-8") as fb:
            fb.write(text)
            return "写入成功"

    def append_txt(self, text=''):
        """
        向txt内容追加写入内容
        :param text: str
        :return: 结果信息
        """
        with open(self.filename, "a+", encoding="utf-8") as fb:
            fb.write(text)
            return '追加内容成功'

    def read_rb_txt(self):
        """
        用字节方式读取txt内容
        :return:
        """
        with open(self.filename, "rb", encoding="utf-8") as fb:
            res = fb.read()
            return res


filename = '1.txt'
t = opr_txt(filename)
res = t.write_txt('12313213')
res1 = t.read_txt()
print(res1)