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

