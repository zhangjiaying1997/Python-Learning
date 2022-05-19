"""
1,os模块:
   1) os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样。
      os模块与os.path模块用于对文件或目录进行操作
   2)os模块操作目录相关函数
   ①getcwd():返回当前的工作目录
   ②listdir(path):返回指定目录下的文件和目录信息
   ③mkdir(path[,mode]):创建目录
   ④makedirs(path1/path2...[,mode]):创建多级目录
   ⑤rmdir(path):删除目录
   ⑥removedirs(path1/path2......):删除多级目录
   ⑦chdir(path):将path设置为当前工作目录
2,os.path模块:
    1)函数:
    ①abspath(path）：用于获取文件或目录的绝对路径
    ②exists(path):用于判断文件或目录是否存在，如果存在返回True,否则返回False
    ③join(path,name):将目录与目录或者文件名拼接起来
    ④splitext():分离文件名和扩展名
    ⑤basename(path):从一个目录中提取文件名
    ⑥dirname(path):从一个路径中提取文件路径，不包括文件名
    ⑦isdir(path):用于判断是否为路径

    walk方法:可以递归遍历所有的文件，不仅可以递归指定目录下的文件，还可以将指定目录下子目录的所有文件列出来,.walk返回来的是一个元组（迭代器对象）
    元组包含的是目录的路径(dirpath)，目录下的文件夹(dirname)和目录下的所有文件(filename)

"""
#os模块与操作系统相关
#1,用os模块打开电脑程序（记事本)
import os
#os.system('calc.exe')

#2，直接调用可执行文件
#os.startfile('H:\\社交软件\\WeChat\\WeChat.exe')

#查看当前目录getcwd()
#path=os.getcwd()
#print(path)
#print(os.listdir('..//文件操作和with语句'))
#os.mkdir('mkdir创建')
#os.rmdir('mkdir创建')
#os.makedirs('A/B/C')
#os.removedirs('A/B/C')
#os.chdir('G:\\Git\\gitcode\\Python-Learning\\文件操作和with语句')
#print(os.getcwd())

#os.path模块操作目录相关函数
#import os
#import os.path as a
#print(a.abspath('courgette.log'))
#print(a.exists('courgette.log'))
#print(a.join('G:\\Git\gitcode\\Python-Learning','courgette.log'))
#print(os.getcwd())
#print(a.split('G:\\Git\gitcode\\Python-Learning'))
#print(a.splitext('courgette.log'))
#print(a.basename('G:\\Git\gitcode\\Python-Learning\\courgette.log'))
#print(a.dirname('G:\\Git\gitcode\\Python-Learning\\courgette.log'))
#print(a.isdir('G:\\Git\gitcode\\Python-Learning'))
#print(a.isdir('G:\\Git\gitcode\\Python-Learning\\courgette.log'))

#列出指定目录下的所有文件
#import os
#path='G:\Git\gitcode\Python-Learning'
#print(os.listdir(path))
#lst=os.listdir(path)
#for filename in lst:
#    if filename.endswith('.py'):    #利用endswith方法来筛选指定扩展名文件
#        print(filename)

#walk方法
import os
path=os.getcwd()
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    #print(dirpath)  #返回目录的路径
    #print(dirname)  #返回文件夹名称
    #print(filename) #返回文件名
    #print('--------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))    #将文件夹路径和文件夹名称连接起来形成所有遍历的文件的文件路径
    for file in filename:
        print(os.path.join(dirpath,file))
    print('-------------------')






