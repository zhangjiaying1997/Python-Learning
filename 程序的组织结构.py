"""
程序组织结构:顺序，选择(if),循环(while,for-in)

顺序结构
分支结构
对象的布尔值
pass空语句
"""

"""
对象的布尔值:
获取对象的布尔值:使用内置函数bool()
以下对象的布尔值为False:
False,数值0，None,空字符串，空列表，空元组，空字典，空集合
"""

"""
 单分支结构：
 if 条件表达式:
 条件执行语句
"""
money=100
if money>=100:
    print('yes ')

"""
双分支结构:
if 条件表达式:
条件执行体1
else:
条件执行体2
"""

time1=3
time2=5
if time1>=time2:
    print('time1>time2')
else:
    print('time1<time2')


"""
多分支结构:
if 条件表达式1:
条件执行体1
elif 条件表达式2:
条件执行体2
elif 条件比倒是N:
条件执行体n
else:
条件执行体N+1
"""

"""
嵌套if
if 条件表达式1:
if 内层条件表达式:
内层条件执行体1
else:
内层条件执行体2
else:
条件执行体
"""

"""
条件表达式:
x if 判断条件 else y
是if else的缩写,意义为如果判断条件为True就返回x,否则返回y
"""
name3=4
print('yes') if name3==4 else print('false')

"""
pass语句：
什么都不做，只是一个占位符，用在语法上需要语句的地方
什么时候使用：先搭建语法结构，还没想好代码怎么写的时候
一般用在什么地方：1，if语句的条件执行体 2，for-in语句的循环体 3，定义函数时的函数体
"""

"""
range()函数：1，用于生成一个整数序列 
2，创建range对象的三种方式:
range(stop):创建一个（0，stop)之间的整数序列步长为1
range(start,stop):创建一个（start，stop)之间的整数序列步长为1
range(start,stop,step):创建一个（start，stop)之间的整数序列步长为step1
返回值是一个迭代器对象
range类型优点:不管range对象表示的整数序列有多长，所有的range对象占用的内存空间都是相同的，因为仅仅需要start,stop,step，只有当用到range对象时才会去计算序列中的相关元素
int和not in判断整数序列中是否存在（不存在）指定的整数
"""

"""
循环结构:
循环的分类：while for-in
语法结构:
while 条件表达式
条件执行体（循环体）

for-in循环：1，in表达从（字符串，序列等)中依次取值，又称为遍历 2，for-in遍历的对象必须是可迭代对象
语法结构：
for 自定义的变量 in 可迭代对象：
循环体
若循环体内不需要访问自定义变量，可以将自定义变量替代为下划线_
"""

"""
流程控制语句break:用于结束循环结构，通常与分支结构if一起使用
流程控制语句continue:用于结束当前循环，进行下一次循环，通常与分支结构中的if一起使用
"""
#a=0
#while a<3:
#    pwd=input('请输入密码:')
#    if pwd=='888888':
#        print('密码正确')
#        break
#    else:
#        print('密码不正确')

"""
else语句：与else语句配合配合使用的情况:
1,if else if条件表达式不成立时执行else
2,while else 没有碰到break时执行else
3,for else 没有碰到break时执行else
"""
for item in range(4):
        print(item)
else:
    print('break for')

"""
嵌套循环: 其中end=’\t‘是不换行输出
二重循环中的Break和continue用于控制本层循环
"""
for item1 in range(10):
    for item2 in range(1,item1+1):
        print(str(item2)+'*'+str(item1),end='\t')
    print('\n')