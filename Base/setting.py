import unittest,time,datetime
import unittest

import os,sys
currentPath = os.path.abspath(os.path.dirname(__file__)) #当前文件夹目录
ProjectPath = os.path.split(currentPath)[0] #项目那个层级的目录
TopPath = os.path.split(ProjectPath)[0] #更上一层目录 假设存在就添加

sys.path.append(ProjectPath) #第一层目录
sys.path.append(TopPath)  #最顶层目录

#second_level = os.path.dirname(os.path.abspath("."))
project_level =os.path.abspath(os.path.dirname(__file__))

#用例路径
# TestDir ="E:\\selenium_uses\\test_case\\"
TestDir=ProjectPath+"\\Run\\"
Debug =False

# print(ProjectPath,TestDir,TopPath)

