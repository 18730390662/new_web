import time,os,datetime
from Base import setting

# BaseDir ="E:\selenium_uses\\Report"  #从setting 文件导入拼接
BaseDir=setting.ProjectPath+"\\Report"
print(BaseDir)

class TimeUtil(object):
    # 日志 报告  拼接事件

    def set_date(self): #固定写法
        now = datetime.datetime.now()
        return "{0}-{1}-{2}".format(now.year, now.month, now.day)

    def set_time(self):#固定写法
        return time.strftime("%H-%M")

    def get_report_path(self): #核心函数
        "格式月日/单位时间格式的.html，只用到time"
        nowtime = time.localtime() #转换为可读的
        dir_date = time.strftime('-%Y%m%d', nowtime) #格式化 Report-年月日
        if not os.path.exists(BaseDir + dir_date): #="E:\selenium_uses\\Report-年月日" 文件夹
            os.mkdir(BaseDir + dir_date)
            #print("路径===》",BaseDir + dir_date)
        day_file = time.strftime('%H%M%S', nowtime)
        return BaseDir + dir_date + '\\' + 'Report-' + day_file + '.html'






