"""
字符串的创建与驻留机制:
字符串: 是不可变的字符序列
字符串的驻留机制:仅保存一份相同且不可变的字符串的方法，不同的值被存放在字符串的驻留池中，Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同的字符串时，
不会开辟新空间，而是把该字符串的地址赋给新创建的变量

1,驻留机制的几种情况(交互模式）：
    1）字符串长度为0或1时
    2）符合标识符的字符串
    3）字符串只在编译时进行驻留，而非运行时
    4）[-5,256]之间的整数数字
2,sys中的intern方法强制2个字符串指向同一对象
3，Pycharm对字符串进行了优化处理

字符串驻留机制的优缺点：
    1）当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，提升效率和节约内存，
    因此拼接字符串和修改字符串是会比较影响性能的。
    2）在需要进行字符串拼接时建议使用str类型的join方法，而非+，因为join()方法是先计算出所有字符中的长度，然后再拷贝，
    只new一次对象，效率要比"+"效率高

字符串的常用操作：
1，字符串的查询操作：
    1）index()方法： 查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError
    2)rindex()方法： 查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
    3)find()方法：  查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1
    3）rfind()方法： 查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1
2,字符串的大小写转换操作的方法
    1）upper()方法:把字符串中所有字符都转成大写字母
    2）lower()方法:把字符串中所有字母都转成小写字母
    3）swapcase()方法:把所有字符串中的大写字母转成小写字母，把所有的小写字母转成大写字母
    4)capitalize()方法： 把第一个字符转换为大学，其余字符转换为小写
    5)title()方法: 把每个单词的第一个字符转换为大学，把每个单词的剩余字符转换为小写
3,字符串内容对齐操作的方法：
    1）center()方法: 居中对齐，第1个参数指定宽度，第2个参数指定填充符，并且第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
    2)ljust()方法:  左对齐，第1个参数指定宽度，第2个参数指定填充符，并且第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
    3)rjust()方法:  右对齐，第1个参数指定宽度，第2个参数指定填充符，并且第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
    4)zfill()方法:  右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身
4,字符串劈分操作的方法:
    1）split()方法：
    ①从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
    ②以通过参数sep指定劈分字符串是的劈分符
    ③通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
    2）rsplit()方法：
    ①从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
    ②以通过参数sep指定劈分字符串是的劈分符
    ③通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
5，判断字符串操作的方法:
    1)isidentifier(): 判断指定的字符是不是合法的标识符
    2)isspace(): 判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
    3)isalpha(): 判断指定的字符串是否全部有字母组成
    4)isdecimal(): 判断指定的字符串是否全部由十进制的数字组成
    5）isnumeric(): 判断只当的字符串是否全部有数字组成
    6)isalnum()： 判断指定字符串是否全部由字母和数字组成
6. 字符串的替换与合并
    1)replace():字符串的替换，第1个参数指定被替换的子串，第2个参数指定替换子串的字符串，该方法返回替换后得到的字符串，
    替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数
    2）join():将列表或元组中的字符串合并成一个字符串,也可将单个字符串中的各个字符隔开连接 ： e.g '|'.join(lst)
7,字符串的比较操作
    1）比较运算符：>,>=,<,<=,==,!=
    2)比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，
    其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
    3）比较原理： 两个字符进行比较时，比较的是其ordinal value(原始值），调用内置函数ord可以得到指定字符的ordinal value.
    与内置函数ord对应的是内置函数chr,调用内置函数chr时指定ordinal value可以得到其对应的字符
8,字符串的切片操作：
    1）字符串时不可变类型，不具备增删改等操作，切片操作将产生新的对象
    e.g: s[start:stop:step] ,截取从start到stop,步长为step的字符串片段，产生的是一个新的字符串对象

9,格式化字符串:
    1)格式化字符串的3种方式：
    ①%作占位符：%s 字符串, %i或%d 整数，%f 浮点数   e.g: '我的名字叫：%s,今年 %d岁了' % (name,age)
    ②{}作占位符:  e.g: '我的名字叫：{0},今年{1}岁了，我真的叫: {0}'.format(name,age)
    ③{}作占位符: e.g: print(f'My name is {name}, this year {age}')  其中字符串前面需要加f来表示这是一个格式化字符串
    2)宽度和精度的设置
    ①； e.g : print('%3d' % 99) 其中3表示宽度为3
    e.g: print('%.3f' % 1.34535) 其中.3表示精确到小数点后3位，表示精度
    e.g: print('%3.3f' % 1.2344) 可以同时表示精度和宽度
    ②: e.g: print('{0:.3}'.format(3.123442))  其中0是表示占位符的顺序, .3表示总共有三位数，即宽度
    e.g: print('{0:.3f}'.format(3.2342342))  其中.3f表示的是保留小数点后3位,即精度
    e.g: print('{0:10.3f}'.format(3.2342532))  其中10表示宽度，.3f表示精度,可以同时表示宽度和精度
10,字符串的编码与解码
    1)encode()方法:编码:将字符串转换为二进制数据(bytes)
    2)decode()方法:解码:将bytes类型的数据转换为字符串类型
    同一种方式编码只能同一种方式解码


"""

#字符串的编码转换
s='张佳颖大帅逼'
print(s.encode(encoding='GBK')) #GBK编码
sg=s.encode(encoding='GBK')
print(sg.decode(encoding='GBK'))
print(s.encode(encoding='UTF-8')) #UTF-8编码
utf=s.encode(encoding='UTF-8')
print(utf.decode(encoding='UTF-8'))
#print(utf.decode(encoding='GBK')) #将会出现解码错误，因为编码和解码方式必须统一




#格式化字符串表示宽度
#print('%8d' % 99)
#print('%.3f' % 3.12345678)
#print('%5.3f' % 123456.1234667)
#print('{0:8d}'.format(99))
#print('{0:.3f}'.format(3.12434554))
#print('{0:3.3f}'.format(12345.1234556))



#格式化字符串
#name='zhangsan'
#age=20
#print('My name is %s, this year %d' % (name,age))
#print('My name is {0},this year {1}'.format(name,age))
#print(f'My name is {name}, this year {age}')



#字符串的切片操作



#字符串的比较操作
#print('apple'>'app')
#print('apple'>'banana')
#print(ord('a'),ord('b'))
#print(ord('张'))
#print(chr(97),chr(98))


#字符串的替换和合并
#s='hello,python'
#print(id(s),s.replace('python','c++'),id(s))
#s1='hello,python,python,python'
#print(s1.replace('python','c++',2))
#print('|'.join(s1))
#lst=['hello','python','python','java']
#print('|'.join(lst))
#print(''.join(lst))
#t=('hello','python','java')
#print('|'.join(t))

#判断字符串操作的方法
#s='hello,Python'
#s1='                \t'
#print(s.isidentifier())
#print(s1.isspace())
#print('zhangsan'.isalpha())
#print('102300450'.isnumeric())
#print('2343552140001234'.isdecimal())
#print('sdffwee234231edwr23df'.isalnum())



#字符串的劈分操作
#s='hello world Python'
#lst=s.split()
#print(lst,type(lst))
#s1='hello|world|Python'
#lst1=s1.split(sep='|')
#lst2=s1.split(sep='|',maxsplit=1)
#print(lst1,type(lst1))
#print(lst2,type(lst2))


#字符串的对齐方法:
#s='hello,Python'
#print(s.center(20,'*')) #居中对齐
#print(s.ljust(20,'&')) #左对齐
#print(s.rjust(20,'&')) #右对齐
#print(s.zfill(20)) #右对齐


#字符串的大小写转换方法
#s='hello,python'
#a=s.upper()
#a=s.lower()  #转换之后会产生一个新的字符串对象，因此地址会跟原来的地址不同，即 a is not s
#a=s.title()
#a=a.swapcase()
#a=a.capitalize()
#print(a,id(a))
#print(s,id(s))



#字符串的驻留机制和字符串的查找操作
#a='Python'
#b="Python"
#c='''Python'''
#d='Pyt'+'hon'
#e=''.join(['Pyt','hon'])
#f='Python,Python'
#print(a,id(a))
#print(b,id(b))
#print(c,id(c))
#print(d is e,id(d),id(e))
#print(f.index('on'))
#print(f.rindex('on'))
##print(f.index('to'))
#print(f.find('on'))
#print(f.rfind('on'))
#print(f.find('ot'))

