#coding=utf-8
from Base import setting
import json
from Utils.handle_json import HandleJson


def get_header(key):
    data = HandleJson(setting.ProjectPath+"/Config/header.json").load_json()
    return data.get(key)

def write_token_value(token,cookie_key):
    """
    :param token:
    :param cookie_key:
    :return:
    """
    h_j = HandleJson(setting.ProjectPath + '/Config/header.json')
    data1 = h_j.load_json()
    data1[cookie_key]["token"] = token
    print(type(data1))

    return h_j.write_json(data1)


def header_md5():
    '''
     加载token
    '''


if __name__ == '__main__':
    a=write_token_value("token1","web")
    data = get_header("web")
    print("1",a)
    print("2",data)


