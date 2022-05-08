#输出字符串，数字,表达式
print('Hello world!')
print('\n')
print(520)
print('\n')
print(4+6)
print('\n')
#将数据输出到文件当中
fp=open('G:/Git/gitcode/Python-Learning/hello2.txt','a+')
print('hello world!',file=fp)
fp.close()