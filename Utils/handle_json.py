# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.getcwd())
base_path = os.path.abspath(os.path.dirname(os.getcwd()))

from Utils.handle_init import handle_ini
import json

class HandleJson(object):
   def __init__(self,file_path=None):
       if file_path == None:
           self.file_path = '/'.join([base_path,'Config/code_message.json'])
       else:
           self.file_path = file_path

   def load_json(self):
       """
       加载json数据
       :return:
       """
       with open(self.file_path,'r',encoding='UTF-8') as f:
           return json.load(f)

   def get_value(self,url):
       """
       获取json数据下，指定url下的数据
       :param url: 操作的接口url
       :return: url下的操作数据
       """
       data = self.load_json()[url]
       return data

   def write_json(self,data):
       """
       向json文件中写入数据
       :param data:
       :return:
       """
       data = json.dumps(data)
       with open(self.file_path,'w') as f:
           f.write(data)



if __name__ == '__main__':
   file_path = '/'.join([base_path, 'Config/header.json'])

   print(HandleJson(file_path).load_json())


#操作对应的code_message.json
# Utils写一个针对meesage+error.json文件的操作方法