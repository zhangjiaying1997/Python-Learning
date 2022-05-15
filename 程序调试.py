"""
1,Bug的常见类型：
    1，语法错误SyntaxError
    1）input输入的均为str类型，如果将其使用到数字，会报错:
    e.g:
    age=input('请输入年龄：')
    if age>=18
    print('----')
    其中input输入的是str类型，但是18是int类型，所有这两者不能比较类型不同，因此会报错
    ①漏了末尾的冒号，如if语句，循环语句，else子句等
    ②缩进错误
    ③把英文符号写成中文符号，比如括号
    ④字符串拼接的时候，把字符串和数字拼在一起
    ⑤没有定义变量
    ⑥==和=的混用
    2,索引越界问题IndexError
    3,程序代码逻辑没有错，只是因为用户误操作或者以下‘例外情况‘而导致的程序崩溃

2,Python的异常处理机制
    1)Python提供了异常处理机制，可以在异常出现时即时捕获，然后内部“消化”，让程序继续运行
    执行流程：
    try:
    可能会出现异常的代码
    except 异常类型 :
    异常处理代码
    2)多个except结构：捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException
    3)try...except...else结构:如果try块中没有抛出异常，则执行else块，如果try中抛出异常,则执行except块
    4)try...except...else...finally结构：finally块无论是否发生异常都会被执行，常用来释放tru块中申请的资源
3,Python常见的异常类型
    1）ZeroDivisionError:除（或取模）零（所有数据类型）
    2）IndexError:序列中没有此索引(index)
    3)KeyError:映射中没有这个键（字典）
    4)NameError:未声明/初始化对象（没有属性）
    5）SyntaxError:Python 语法错误
    6）ValueError:传入无效的参数
4，traceback模块：使用traceback模块打印异常信息
    e.g:
    import traceback
    try:
    ......
    except:
    traceback.print_exc()
5,PyCharm开发环境的调试




"""
#Pycharm的程序调试
#i=1
#while i<10:
#    print(i)
#    i+=1


#traceback模块打印异常信息
#import traceback
#try:
#    print('------------')
#    print(1/0)
#except:
#    traceback.print_exc()



#try-except-else-finally结构
#try:
#    n1=int(input('Enter the first number:'))
#    n2=int(input('Enter the first number:'))
#    result=n1/n2
#except BaseException as e:
#    print('出错了')
#    print(e)    #打印出产生的异常原因
#else:
#    print('结果是:',result)
#finally:
#    print('无论是否产生异常，总会执行的代码')
#print('程序结束')



#try-except-else和except-else-finally结构
#try:
#    a=int(input('Enter the first number:'))
#    b=int(input('Enter the second number:'))
#    result=a/b
#except BaseException as e:  #将出错的情况都列为一类，as e是表示所有的BaseException出错情况都取别名为e
#    print('出错了',e)
#else:
#
#    print('计算结果为:',result)



#异常处理机制

#try:
#    a = int(input('Enter the first one number:'))
#    b = int(input('Enter the seconde number:'))
#    result = a / b
#    print('the result is: ', result)
#except ZeroDivisionError:
#    print('除数不能为0')
#    print('程序结束')
#except ValueError:
#    print('只能输入数字')
#    print('程序结束')
#except BaseException:
#    print('其他异常情况')
#    print('程序结束')



