"""
列表：是一个大容器，可以存储N多个元素，程序可以方便地对这些数据进行整体操作,列表相当于其他语言中的数组

列表创建方式:
1,使用中括号[],元素之间使用英文的逗号进行分隔
2,调用内置函数list()

列表的特点：
1,列表元素按顺序有序排列
2,索引映射唯一一个数据
3，列表可以存储重复数据
4，任意数据类型混存
5,根据需要动态分配和回收内存

获取列表中单个元素的索引方式：
列表名字.index(元素值) eg lst.index('hello')
1，从前往后，即从第一个是-1开始
2，从后往前，即从最后一个是-1开始
3,指定元素不存在，抛出IndexError

列表的查询操作:
1,获取指定元素中的索引
    1）如果列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
    2)如果查询的元素在列表中不存在，则会抛出ValueError
    3)还可以在指定的start和stop之间进行查找

获取列表中的多个元素
语法格式:
列表名[start:stop:step]
1,切片的结果是原列表片段的拷贝
2,step为正数（负数）:正数是从start开始往后计算切片，负数是从start开始往前计算切片
    1)[:stop:step]:切片的第一个元素默认是列表的第一个元素
    2）[start::step]切片的最后一个元素默认是列表的第一个元素

列表元素的查询操作：
1,判断指定元素在列表中是否存在 in 和not in
2,列表元素的遍历
for 迭代变量 in 列表名:
操作

列表元素的添加操作:
append()：在列表的末尾添加一个元素
extend():在列表末尾至少添加一个元素
insert():在列表任意位置添加一个元素
切片：在列表的任意位置添加至少一个元素

列表元素的删除操作
remove(): 1，一次删除一个元素，2，重复元素只删除第一个 3，元素不存在则抛出ValueError
pop(): 1,删除一个指定索引位置上的元素 2,指定索引不存在则抛出ValueError 3,不指定索引，删除列表最后一个元素
切片：一次至少删除一个元素
clear():清空列表
del():删除列表

列表元素的修改操作:
1,为指定索引的元素赋予一个新值
2，为指定的切片赋予一个新值

列表元素的排序操作:
1，常见的两种方式：
1）调用sort()方法，列中所有的元素默认按照从小到大的顺序进行排序，可以指定reverse=True,进行降序排序
2)调用内置函数sorted(),可以指定reverse=True，进行降序排序，原列表不发生改变

列表生成式:
语法格式:
[i*i for i in range(1,10)] :其中i*i表示列表元素表达式 i是自定义变量 range(1,10)为可迭代对象

"""
lst2=['helo','sgsdg',23,93,4]
lst=[i for i in range(1,10)] #生成1到9的列表
lst1=[i for i in range('hello')]
print(lst)
#lst=[20,40,10,98,54]
#print('排序前的列表',lst,id(lst))
#lst.sort()
#print('排序后的列表',lst,id(lst))
#lst.sort(reverse=True)
#print('使用reverse=True降序排序后的列表',lst,id(lst))
#
##调用内置函数sorted()进行排序
#lst=sorted(lst)
#print('sorted()排序后的列表',lst,id(lst))
#lst=sorted(lst,reverse=True)
#print('sorted()降序排列后的列表',lst,id(lst))
#lst=[10,20,30,40]
#lst[2]=100
#print(lst)
#lst[1:3]=[300,400,500,600] #其中切片不要求元素个数等于列表长度
#lst[1:3]=[1]
#print(lst)
#lst1=['h','j']
#lst=[10,20,30]
#lst1[2::]=lst
#print(lst1)
#print('after remove（）:')
#lst1[1:3:]=[] #切片就是使批量删除的成片数据赋值为[]空
#lst1.clear()
#del lst1
#print(lst1)
#lst=['hello','world',98]
#print(id(lst))
#print(type(lst))
#print(lst)
#lst2=list(['hello','world',98])
#print(id(lst2))
#print(type(lst2))
#print(lst2)