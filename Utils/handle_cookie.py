# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.getcwd())
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
from Utils.handle_json import HandleJson

def get_cookie_value(cookie_key):
    """
    获取到cookie.json中的指定的cookie串
    :param cookie_key:指定串的键
    :return:cookie串
    """
    data = HandleJson(base_path+'/Config/cookie.json').load_json()
    return data.get(cookie_key)

def write_cookiess_value(data,cookie_key):
    """
    获取到cookie.json中指定的cookie串，将指定的串替换为data，起到一个更新cookie.json的作用
    :param data: 获取到的cookie
    :param cookie_key: 用于指定cookie.json的部分串
    :return:
    """
    h_j = HandleJson(base_path+'/Config/cookie.json')
    data1 = h_j.load_json()
    data1[cookie_key] = data
    h_j.write_json(data1)

if __name__ == '__main__':

    z=get_cookie_value("app")
    b=write_cookiess_value("web","web")
    print(z)





