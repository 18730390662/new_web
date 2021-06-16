#coding=utf-8
import os,sys,unittest
sys.path.append(sys.path[0]+'\..')
from Utils import HTMLTestRunner

currentPath = os.path.abspath(os.path.dirname(__file__)) #当前文件夹目录
ProjectPath = os.path.split(currentPath)[0] #项目那个层级的目录




if __name__ == "__main__":
    case_path = ProjectPath + "/Run"
    report_path = ProjectPath + "/Report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is test", description=" test")
        runner.run(discover)
