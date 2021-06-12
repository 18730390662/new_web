# coding=utf-8
import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)
import ddt
import unittest
import json
from Utils.handle_depend_excel import excel_method
from Utils.handle_header import get_header, write_token_value
from Utils.handle_init import HandleInit
from Utils.handle_result import handle_mr_json, handle_constrast_json, handle_json_json
from Utils.handle_cookie import get_cookie_value
from Utils.codition_data import get_data
from Base.base_requests import request
from Base import setting
from Utils import HTMLTestRunner

data = excel_method.get_excel_data()


@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self, data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        is_run = data[HandleInit().get_int_value('is_run')]
        case_id = data[HandleInit().get_int_value('case_id')]
        i = excel_method.get_row_number(case_id)
        if is_run == 'yes':
            is_depend = data[HandleInit().get_int_value('is_depend')]
            data1 = json.loads(data[HandleInit().get_int_value('data1')])
            try:
                if is_depend:
                    '''
                    获取依赖数据
                    '''
                    depend_key = data[HandleInit().get_int_value('depend_key')]
                    depend_data = get_data(is_depend)
                    # print(depend_data)
                    data1[depend_key] = depend_data

                method = data[HandleInit().get_int_value('method')]
                url = data[HandleInit().get_int_value('url')]

                is_header = (data[(HandleInit().get_int_value('is_header'))])
                excepect_method = data[HandleInit().get_int_value('expect_method')]
                excepect_result = data[HandleInit().get_int_value('except_result')]
                cookie_method = data[(HandleInit().get_int_value('cookie_method'))]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie = {"is_cookie": "app"}
                if is_header == 'yes':
                    header = get_header("app")

                print(get_cookie)
                res = request.run_main(method, url, data1, cookie, header,get_cookie=get_cookie)
                print(res)
                #根据实际情况写入
                # if is_header=="write":
                #     token=res["token"]
                #     write_token_value(token,"web")

                # #根据实际情况写入
                code = int(res.get('error_code'))
                message = res['error_code']
                # message+errorcode

                if excepect_method == 'mec':
                    config_message = handle_mr_json(url, code)
                    '''
                        if message == config_message:
                            excel_data.excel_write_data(i,13,"通过")
                        else:
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(message, config_message)
                        excel_method.excel_write_data(i, 13, "通过")
                        excel_method.excel_write_data(i, 14, json.dumps(res))
                    except Exception as e:
                        excel_method.excel_write_data(i, 13, "失败")
                        raise e

                if excepect_method == 'errorcode':
                    '''
                    if excepect_result == code:
                        excel_data.excel_write_data(i,14,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(excepect_result, code)
                        excel_method.excel_write_data(i, HandleInit().get_int_value('actual_result'), "通过123")
                        excel_method.excel_write_data(i, HandleInit().get_int_value('result_data'),
                                                      json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_method.excel_write_data(i, 13, "失败")
                        raise e
                if excepect_method == 'json':

                    if code == 1000:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = handle_json_json(url, status_str)
                    result = handle_constrast_json(res, excepect_result)
                    '''
                    if result:
                        excel_data.excel_write_data(i,13,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))   
                    '''
                    try:
                        self.assertTrue(result)
                        excel_method.excel_write_data(i, 13, "通过")
                    except Exception as e:
                        excel_method.excel_write_data(i, 13, "失败")
                        raise e
            except Exception as e:
                excel_method.excel_write_data(i, 13, "失败")
                raise e


if __name__ == "__main__":
    case_path = base_path + "/Run"
    report_path = base_path + "/Report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is test", description=" test")
        runner.run(discover)