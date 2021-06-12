#coding=utf-8
import sys
import os
sys.path.append(os.getcwd())
base_path = os.path.abspath(os.path.dirname(os.getcwd()))

from Utils.handle_json import HandleJson


def get_token_header():
    data = HandleJson(base_path+"/Config/token_header.json").load_json()
    return data


def header_updata_token_header(token):
    data=get_token_header()
    data["token"]=token
    return data


if __name__ == '__main__':
   print(header_updata_token_header(12))
   print(get_token_header())