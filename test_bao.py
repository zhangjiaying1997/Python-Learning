"""
在test_bao文件中导入包bao
"""
import bao.module_A as a    #a是bao.module_A的别名
from bao.module_B import b as bb
print(a.a)  #第一个a是bao.module_A的别名，第二个a是module_A里面的变量
print(bb)

#导入标准库模块
import sys
import time
import urllib.request as ur
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(time.time())
print(time.localtime(time.time()))
print(ur.urlopen('http://www.baidu.com').read())
import schedule
def job():
    print('哈哈-----------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
