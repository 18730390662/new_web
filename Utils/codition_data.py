# coding=utf-8
import os
import sys

sys.path.append(os.getcwd())
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
from Utils.handle_depend_excel import excel_method
from jsonpath_rw import parse
import json


def split_data(data):
    '''
    拆分单元格数据
    '''
    # imooc_005>data:banner:id
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id, rule_data


def depend_datas(data):
    '''
    获取依赖结果集

    '''
    case_id = split_data(data)[0]
    row_number = excel_method.get_row_number(case_id)
    data = excel_method.get_cell_value(row_number, 15)
    return data


def get_depend_data(res_data,key):
    '''
    获取依赖字段
    '''


    res_data = json.loads(res_data)

    json_exe = parse(key)
    madle = json_exe.find(res_data)
    return [math.value for math in madle][0]


def get_data(data):
    '''
    获取依赖数据
    '''
    res_data = depend_datas(data)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data, rule_data)


if __name__ == "__main__":

    print(get_data("imooc_007>outstr"))
    data = {
        "a":"a1",
        "b":"b1",
        "c":[
            {
                "d":"d1"
            },
            {
                "d":"d2"
            }
        ]
    }
    key = 'a'
    print(get_depend_data(data,key))





