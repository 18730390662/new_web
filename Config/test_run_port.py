# coding=utf8
import os
import sys
sys.path.append(os.getcwd())
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
# 用例路径
case_path = os.path.join(os.getcwd())
# 报告存放路径
report_path = os.path.join(os.getcwd(), 'report')
from Run import HTMLTestRunner
import ddt

from Utils.handle_depend_excel import *
from Utils.handle_init import HandleInit
from Base.base_requests import request
import json,unittest,time
from Utils.handle_result import handle_mr_json,handle_constrast_json,handle_json_json
from Utils.handle_cookie import get_cookie_value,write_cookiess_value
from Utils.handle_header import get_header
from Utils.hadle_token import get_token_header,header_updata_token_header
from Utils.handle_json import HandleJson
from Utils.codition_data import get_data,get_depend_data,depend_datas

data = excel_method.get_excel_data()
print(data)

@ddt.ddt
class testRunMain(unittest.TestCase):
    """
    用例执行的主函数
    """

    @ddt.data(*data)
    def test_main_case(self,data):
        #获取用例数
        lines = excel_method.get_rows()
        for i in range(lines-1):
            cookie = None
            get_cookie = None
            header = None
            depend_data=None
            #----------拿取Excel所有每一行数据---------
            data_list = excel_method.get_row_data(i+2)
            # print(data_list)
            #------基本搭建 ---
            is_run = data_list[HandleInit().get_int_value('is_run')]
            if is_run == 'yes':
                # data1 = ast.literal_eval(data_list[HandleInit().get_int_value('data1')])
                data1 = json.loads(data_list[HandleInit().get_int_value('data1')])
                is_depend = data_list[HandleInit().get_int_value('is_depend')]
                case_id = data_list[HandleInit().get_int_value('case_id')]
                try:

                    if is_depend:
                        depend_key=data_list[HandleInit().get_int_value('depend_key')]

                        depend_data = get_data(is_depend)

                        data1[depend_key] = depend_data


                        # data1[depend_key] = 'depend_data'
                        #找到depend value
                        # depend_value=get_depend_data(is_depend, key)
                    case_id=data_list[HandleInit().get_int_value('case_id')]
                    method = data_list[HandleInit().get_int_value('method')]
                    url = data_list[HandleInit().get_int_value('url')]

                    # print(type(params)) #验证数据格式是否为字典
                    cookie_method=data_list[(HandleInit().get_int_value('cookie_method'))]
                    print(cookie_method)
                    is_header=(data_list[(HandleInit().get_int_value('is_header'))])
                    print("is_header yes需要设定格式",is_header)
                    #-----token---
                    write_token_to_header = (data_list[(HandleInit().get_int_value('write_token_to_header'))])
                    print('write_token_to_header token是否写入',write_token_to_header)




                    if cookie_method == "yes":
                        #读取固定cookies
                        cookie = get_cookie_value('app')
                        print("这是cookie",cookie)

                    if cookie_method == "write":
                        #将cookies 写入
                        get_cookie={"is_cookie":"web"}
                        print("这是要写入的",get_cookie)

                    if cookie_method == "no":
                        cookie = ""

                    if is_header == "yes":
                        #修改仅仅需要传入header格式,可以固定写死的 例如 header={"Content-Type": "application/json"}

                        header = get_header()
                        print("这是header",header)

                    if is_header=="need_token":
                        #header需要传入token
                        header=header_updata_token_header(token)
                        print("need_token:token传header",header)


                    res = request.run_main(method, url, data1,header,cookie,get_cookie)


                    #token处理
                    if write_token_to_header=="write":
                        #header可以将其他值纳入header
                        token=res['token']
                        self.header=header_updata_token_header(token)
                        print("header_updata_token_header(token)",header_updata_token_header(token))


                   # ---------------------断言开始-------------------------------------

                    except_method=data_list[HandleInit().get_int_value('expect_method')]
                    except_result=data_list[HandleInit().get_int_value('except_result')]

                    errorcode = res.get('error_code')
                    # print("errorcode1",res["error_code"])
                    print("预期",except_result)
                    print("code",errorcode)
                    print("res",type(res))
                    print(type( json.dumps(res,ensure_ascii=False)))
                    #返回结果里的数据{'error_code': 0, 'reason': 'Return Successd!', 'instr': 'csdn论坛Millet接口自动化测试', 'outstr': 'csdn論壇Millet-接口自動化測試'}
                    #{"code": "200", "message": "登录成功", "token": "3768e8cf0c1bd64028eee6c2d44e100a340c914c68e71cb76c93b4931259c3aa" ｝

                    if except_method=="errorcode+message":
                        # errorcode+messaged断言方式
                        message=res.get('message')
                        print("message",message)
                        except_message=handle_mr_json(url,errorcode)
                        if message==except_message:
                            print('{}--->{}---except_message---->pass'.format(case_id,except_method))
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "恭喜通过")
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))
                        else:
                            print('{}------except_message---->fail'.format(case_id))
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "失败")
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))

                    if except_method == "json":
                        if errorcode == except_result: #if errorcode == 0: 不建议写死。因为每个接口成功的返回值不固定
                            status_code = "success"        #
                        else:
                            status_code = "error"
                        result=handle_constrast_json(res,handle_json_json(url,status_code))

                        if result == True:
                            print('{}--->{}--->pass'.format(case_id,except_method))
                            excel_method.excel_write_data(i + 2,HandleInit().get_int_value('actual_result'), "通过")
                            excel_method.excel_write_data(i + 2,HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))

                        else:
                            print(print('{}--->except_message--->failure'.format(case_id)))
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "失败")
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))

                    if except_method == 'errorcode':
                        '''
                        if excepect_result == code:
                            excel_data.excel_write_data(i,14,"通过")
                        else:
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                        '''
                        try:
                            self.assertEqual(except_result, errorcode)
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "通过123")
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'),
                                                          json.dumps(res, ensure_ascii=False))
                        except Exception as e:
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "失败")
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'),
                                                          json.dumps(res, ensure_ascii=False))
                            raise e
                    # if except_method == "errorcode":
                    #
                    #    if int(except_result) == int(errorcode):
                    #        print('{}--->except_message--->pass'.format(case_id,except_method))
                    #        excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "通过123")
                    #        excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))
                    #        print("json.dumps(res,ensure_ascii=False)", type(json.dumps(res,ensure_ascii=False)))
                    #    else:
                    #         print(('{}--->except_message--->failure'.format(case_id,except_method)))
                    #         excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "失败")
                    #         excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))


                    if except_method == "in":
                        if except_result != None :  # if errorcode == 0: 不建议写死。因为每个接口成功的返回值不固定
                            status_code = "success"  #
                        else:
                            status_code = "error"
                        result = handle_constrast_json(res, handle_json_json(url, status_code))
                        print("status_code)",status_code)

                        if result == True:
                            print('{}--->{}--->pass'.format(case_id, except_method))
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "通过")
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))
                        else:
                            print(('{}--->except_message--->failure'.format(case_id, except_method)))
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "失败")
                            excel_method.excel_write_data(i + 2, HandleInit().get_int_value('result_data'), json.dumps(res,ensure_ascii=False))
                except Exception as e:
                    excel_method.excel_write_data(i + 2, HandleInit().get_int_value('actual_result'), "用例允许执行，但是失败了")
                    raise e


                #-------------------------------断言结束------------------------------

if __name__ == '__main__':
    case_path = base_path + "/R"
    report_path = base_path + "/Report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_case_*.py")
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Mushishi", description="this is test")
        runner.run(discover)
