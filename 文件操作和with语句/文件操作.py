#Encoding=utf-8
"""
1,编码格式介绍：
    1）Python的解释器使用的是Unicode(内存)
    2).py文件在磁盘长使用UTF-8存储(外存)
    3).py文件要转换编码存储，需要在最开始加一句:
        #Encoding=编码格式(gbk或utf-8)
2,文件的读写原理_读取磁盘文件中的内容
    1)读文件
        ①内置函数open()创建文件对象，通过IO流将磁盘文件中的内容与程序对象中的内容进行同步
        ②语法规则:
            file=open(filename [,mode,encoding])
            file:被创建的文件对象   open():创建文件对象函数     filename:要创建或打开的文件名称        mode:打开模式，默认为只读
            encoding:默认文本文件中字符的编写格式为gbk
    2)常用的文件打开模式
        ①文件类型：
            文本文件：存储的是普通”字符“文本，默认为unicode字符集，可以使用记事本程序打开
            二进制文件：把数据内容用”字节“进行存储，无法用记事本打开，必须使用专用的软件打开，e.g: mp3音频文件，jpa图片.doc文档等
        ②打开模式：
            Ⅰ,r :以只读模式打开文件，文件的指针将会放在文件的开头
            Ⅱ，w :以只写的模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
            Ⅲ，a :以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追加内容，文件指针在文件末尾
            Ⅳ，b :以二进制方式打开文件，不能单独使用，需要与其它模式一起使用, e.g: rb或wb
            Ⅴ，+ :以读写方式打开文件，不能单独使用，需要与其它模式一起使用，e.g: a+
    3)文件对象的常用方法:
        ①read([size]):从文件中读取size个字节或字符的内容返回，若省略[size],则读取到文件末尾，即一次读取文件所有内容
        ②readline():从文本文件中读取一行内容
        ③readlines():把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
        ④write(str):将字符串str内容写入文件
        ⑤writelines(s_list):将字符串列表s_list写入文本文件，不添加换行符
        ⑥seek(offset[,whence]):把文件指针移动到新的文章，offset表示相对whence的位置：
            offset:为正往结束方向，为负往开始方向移动
            whence不同的值代表不同含义：
            0:从文件头开始计算（默认值)
            1：从当前位置开始计算
            2:从文件尾开始计算
        ⑥tell():返回文件指针的当前位置
        ⑦flush():把缓冲区的内容写入文件，但不关闭文件
        ⑧close():把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源
    4)with语句(上下文管理器):with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确关闭，以此来达到释放资源的目的
    格式：
    with open('logo.png','rb') as src_file:
        src_file.read()
    其中 with 后跟的是一个对象（记住Python中一切皆对象） open（）函数将创建一个文件对象  as后跟的是创建对象的别名src_file
    with下面的语句体部分跟的是对创建对象的操作
    整个过程中，open()函数是上下文表达式，创建的对象是上下文管理器，遵循了上下文管理协议（实现了__enter__()和__exit__()方法）
    创建运行时上下文的时候自动调用__enter__()方法并将返回值赋给src_file
"""
#创建文件
#file=open('a.txt','r')
#print(file.readlines())
#file.close()
#常用文件打开模式
#file=open('b.txt','w')
#file.write('Python')
#file.close()
#file=open('b.txt','a')
#file.write('Python')
#file.close()

#打开并复制二进制数据文件
#src_file=open('../其他文件的打开/1.jpeg', 'rb')
#target_file=open('copy1.jpeg','wb')
#print(target_file.write(src_file.read()))   #边读边写
#target_file.close()
#src_file.close()

#file=open('a.txt','r')
#print(file.read(2))
#print(file.readlines())
#file.close()

#file=open('c.txt','a')
##file.write('hello')
#lst=['java','c++','Python']
#file.writelines(lst)
#file.close()

#file=open('a.txt','r')
#file.seek(2)    #utf-8编码中汉字占2个字节,所有在不同编码环境中seek中如果是1将会报错
#print(file.read())
#print(file.tell())
#file.close()

#使用with语句自动管理资源
#with open('a.txt','a+') as src_file:
#    src_file.write('\nthis is MrZ')
#class MyContentMgr(object):
#    def __enter__(self):
#        print('enter方法被调用执行了')
#        return self
#    def __exit__(self, exc_type, exc_val, exc_tb):
#        print('exit方法被调用执行了')
#    def show(self):
#        print('show方法被调用执行了',1/0)   #即使产生了异常，__exit__()方法任然会执行，所以无论是否产生异常，上下文管理器都会调用__exit__（）方法退出
#
#with MyContentMgr() as file:
#    file.show()

#使用with语句实现图片的copy
with open('../其他文件的打开/1.jpeg', 'rb') as src_file:
    with open('2.jpeg','wb') as target_file:
        target_file.write(src_file.read())






