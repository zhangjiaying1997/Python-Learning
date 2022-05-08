#转义字符
print('hello\nworld') # \ +转义功能的首字母 n->newline的首字符表示换行
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld') # \r是退格字符 world 对hello进行了覆盖
print('hello\bworld') # \b是退一个格，将o退没了

print('http:\\\\www.baidu.com') #其中\\只表示一个\，因为要转义
print('老师说：\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
print(r'hello\nworld')
#注意事项，最后一个字符不能是反斜杠\
print(r'hello\nworld\\')


#查询unicode汉字编码表转换字符
print(chr(0b100111001011000))
print(ord('乘'))

#python中的标识符和保留字 规则：1，以字母，数字，下划线组成 2，不能以数字开头 3，不能是保留字 4，区分大小写

#变量的定义和使用 变量由三部分组成：1，标识：表示对象所存储的内存地址，使用内置函数id(obj)来获取 2,类型：表示对象的数据类型，使用内置函数type(obj)来获取 3，值：表示对象所存储的具体数据，使用print(obj)可以将值答应输出
name='玛丽亚'
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)

#变量多次赋值，变量名会指向新的空间
name2='mar'
print('name:',name2,' id',id(name2))
name2='bet'
print('name:',name2,' id',id(name2))