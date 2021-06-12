#coding=utf-8
import sys
import os
import configparser # pip install ConfigParser

sys.path.append(os.getcwd())
base_path = os.path.abspath(os.path.dirname(os.getcwd()))


class HandleInit:
    def load_ini(self):
        file_path = base_path+"//Config//server.ini"
        cf=configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf


    def get_value(self,key,node=None):
        '''
        获取ini里面的value
        '''
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node,key)
        except Exception:
            print("没有获取到值")
            data = None
        return data

    def get_int_value(self, key, section=None):
        """
        对于返回值的数字做一个数字型处理
        :param key:
        :param section:
        :return:
        """
        value = self.get_value(key, section)
        value = int(value)
        return value


handle_ini = HandleInit()
# a=handle_ini.get_value("host")
# print(a)

if __name__ == "__main__":
    print(handle_ini.get_value('host'))
    print(handle_ini.get_value('cookie_method'))
    # pass
    # hi = HandleInit()
    # print(hi.get_value("password"))
    # print(hi.get_value('host'))
    # hi.get_value(node,'host')






