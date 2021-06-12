import os
import sys
sys.path.append(os.getcwd())
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
from Utils.handle_json import HandleJson
from deepdiff import DeepDiff


def handle_mr_json(url,errorcode):
    # errorcode + message 错误码
    errorcode = str(errorcode)
    data = HandleJson(base_path+'/Config/code_message.json').get_value(url)
    if data != None:
        return [i.get(errorcode) for i in data if i.get(errorcode)][0]


# 添加对比方法和对两个json格式对比效验的方法
def handle_json_json(url,status_code):
    # json格式效验 正常
    status_code = str(status_code)
    data = HandleJson(base_path+'/Config/construction_result.json').get_value(url)
    if data != None:
        return [i.get(status_code) for i in data if i.get(status_code)][0]

def handle_constrast_json(dict1,dict2):
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        if cmp_dict.get('dictionary_item_added'):
            return False
        else:
            return True
    return False






if __name__ == '__main__':
    print(handle_mr_json('charconvert/change.from', 206901))
    print(handle_json_json('charconvert/change.from', "success"))
    dict1={'error_code': 0, 'reason': 'Return Successd!', 'instr': 'csdn论坛Millet-接口自动化测试', 'outstr': 'csdn论坛Millet-接口自动化测试'}
    dict2={'error_code':"", 'reason': "", 'instr': '', 'outstr': ''}
    a=handle_constrast_json(dict1,dict2)
    print(a)
# 三种校验方式


