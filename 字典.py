"""
字典: 1,Python内置的数据结构之一，与列表一样是一个可变序列 2,以键值对的方式存储数据，字典是一个无序的序列
字典是根据key查找value所在的位置

字典的创建:
1,使用花括号{} e.g: scores={'张三':100,'李四':98,'王五':45}
2,使用内置函数dict(): e.g: dict(name='jack',age=20)

字典中元素的获取
1, [] :如果字典中不存在指定的key,抛出keyError异常
2, get()方法 :如果字典中不存在指定的key,并不会抛出KeyError而是返回None,可以通过参数设置默认的value,以便指定的key不存在时返回
3,字典的特点:
    1)字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
    2)字典中的元素是无序的
    3)字典中的key必须是不可变对象
    4)字典也可以根据需要动态的伸缩
    5)字典会浪费均较大的内存，是一种使用空间换时间的数据结构

字典的常用操作：
1,字典的删除: del scores['zhangsan']
2,字典的新增: scores['jack']=90
3,元素是否在字典中: in和not in
4,字典元素修改: 直接赋值即可
5,获取字典试图的三个方法:
    1)keys() ：获取字典中所有的key
    2)values(): 获取字典中所有的value
    3)items(): 获取字典中所有的key,value对

字典元素的遍历:
for item in scores:
print(item)
获取的是字典里的键(key)

字典生成式:
内置函数zip()：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回有这些元组组成的列表
{item.upper(): price for item,price in zip(items,princes)} :
item.upper()：表示字典key的表达式
price:表示value的表达式
item:自定义表示key的变量
price:自定义表示value的变量
items和prices都是可迭代对象

"""

#字典生成式
items=['Fruits','books','nice']
prices=[23,45,23,45,23]
d={item.upper():price for item,price in zip(items,prices)}
print(d)

#字典元素的遍历
#scores={'zhangsan':100,'lisi':98,'wangwu':45}
#for item in scores:
#    print(item,scores[item],scores.get(item))


#scores={'zhangsan':100,'lisi':98,'wangwu':45}
#kkey=scores.keys()
#print(kkey,id(scores),id(kkey),type(kkey))
#print(kkey,list[kkey],type(list[kkey]))
#print(scores.values())
#print(scores.items())
#print(list(scores.items()),type(list(scores.items()))) #转换之后的列表元素是由元组组成

#scores={'zhangsan':100,'lisi':98,'wangwu':45}
#print('zhangsan' in scores)
#print('lili' not in scores)
#del scores['zhangsan']
#print(scores)
#scores['zhangsan']=10
#print(scores)
#scores['zhangsan']=12
#print(scores)



#使用{}创建字典
#scores={'zhangsan':100,'lisi':98,'wangwu':45}
#print(scores)
#student=dict(name='jack',age=20)
#print(student)

#使用[]获取字典元素
#print(scores['zhangsan'])
#print(scores['zsn'])
#使用get()方法
#print(scores.get('zhangsan'))
#print(scores.get('san'))
#print(scores.get('ma',77))  #get可以指定如果不存在的话返回的值


