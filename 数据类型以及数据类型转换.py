#数据类型：整型，浮点型，布尔类型，字符串类型

#整型： 0b:二进制 0o:八进制 0x:十六进制
import decimal

n1=90
n2=-90
n3=0
print(n1,type(n1),n2,type(n2),n3,type(n3))
print('十进制',113)
print('二进制',0b10101111)
print('八进制',0o176)
print('十六进制',0x1EAF)

#浮点型 浮点数存储不精确：使用浮点数进行计算，可能会出现小鼠位数不确定的情况。 解决办法：导入模块decimal
n1=1.1
n2=2.2
print(n1+n2)

from decimal import Decimal #decimal模块
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型 布尔值可以转成整数计算
f1=True
f2=False
print(f1)
print(f2)
print(f1+f2)

#字符串类型 ：不可变的字符序列 可以使用单，双，三引号来定义 ，单双引号定义可以在同一行，三引号可以分布在连续的多行
str1='人生苦短，我用Python'
str2="人生苦短，我用Python"
str3='''人生苦短，
我用Python'''
str4="""人生苦短，
我用Python"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))

#类型转换_str()函数与int()函数，float()函数
name='张三'
age=20

print(type(name),type(age)) #说明name与age的数据类型不相同
#print('我叫'+name+'今年'+age) #TypeError: 'module' object is not callable 只能连接相同类型，所以需要数据类型转换
print('我叫'+name+'今年'+str(age))
print('---------str()将其他类型转换成str类型----------') #str()也可用引号转换
a=10;b=198.8;c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
print('10',type('10'))

#int()将其他类型转换成int类型
s1='126';f1=98.7;s2='76.77';ff=True;s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(3))
print(int(s1),type(int(s1))) #将str转换成int类型,字符串为数字串
print(int(f1),type(int(f1))) #将float转换成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2))) #将str转换成int类型，字符串为小数串,报错，因为字符串为小数串
print(int(ff),type(int(ff))) #将bool转换成int类型，True为1，False为0
#print(int(s3),type(int(s3))) #报错，将str转换成int类型时，字符串必须为数字串（整数),非数字串是不允许转换

#float()将其他类型转换成float类型 1，文字类无法转换成整数 2，整数转换成浮点数，末尾为.0
print('--------------float()，将其他数据类型转换成float类型')

s1='128.98';s2='76';ff=True;s3='Hello';i=98
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3))) #报错，文字类无法转换成整数
print(float(i),type(float(i)))






