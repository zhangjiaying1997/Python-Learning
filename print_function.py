#输出字符串，数字,表达式
print('Hello world!')
print('\n')
print(520)
print('\n')
print(4+6)
print('\n')
#将数据输出到文件当中 ,注意点。1，所指定的盘符存在， 2，使用file=fp
fp=open('G:/Git/gitcode/Python-Learning/hello2.txt','a+') #如果文件不存在就创建，存在即在文件内容的后面继续追加（a+)
print('hello world!',file=fp)
fp.close()
#不进行换行输出，输出内容在一行当中
print('hello','world','Python')