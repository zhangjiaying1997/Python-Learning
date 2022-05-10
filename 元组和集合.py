"""
不可变序列和可变序列：
1，不可变序列：字符串，元组   没有增删改查的操作
2,可变序列：列表，字典  可以对序列执行增删改操作，对象地址不发生更改

元组:Python内置的数据结构之一，是一个不可变序列

元组的创建方式:
1,直接使用小括号   e.g: t=('Python','hello',90)
2,使用内置函数tuple()   e.g:t=tuple(('Python','hello',90))
3,只包含一个元组的元素需要使用逗号和小括号

为什么要将元组设计成不可变序列
1,在多任务环境下，同时操作对象时不需要枷锁
2，因此，在程序中尽量使用不可变序列
注意事项:
1元组中存储的时对象的引用
a)如果元组中对象本身是不可变对象，则不能再引用其它对象
b)如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变

元组的遍历：
元组是可迭代对象，所以可以使用for in 进行遍历
e.g:
t=tuple(('Python','hello',90))
for item in t:
print(item)

集合的概述与创建
集合：
1，是Python 提供的内置数据结构
2,与列表，字典一样都属于可变类型的序列
3,集合是没有value的字典
4,集合中的元素不允许重复

集合的创建：
1，直接使用{}
2,使用内置函数set() :使用set()创建集合，并且将列表，字符串等可迭代对象转换为集合元素，转换后自动去除重复元素，并且是无序集合
3,创建一个空集合只能使用set() ,即s=set(),而不能使用s={}，s={}创建的是一个空字典
3,创建一个空集合只能使用set() ,即s=set(),而不能使用s={}，s={}创建的是一个空字典
3,创建一个空集合只能使用set() ,即s=set(),而不能使用s={}，s={}创建的是一个空字典""

集合的相关操作：
1，集合的判断操作：in和not in
2,集合的新增操作:
    1)调用add()方法，一次添中一个元素
    2）调用update方法：至少添中一个元素
3，集合的删除操作：
    1）调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
    2)调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛异常
    3）调用pop()方法，一次只删除一个任意元素
    4）调用clear()方法，清空集合

集合间的关系：
1，两个集合是否相等: 使用==和！=进行判断
2，一个集合是否是另一个集合的子集: 调用方法issubset进行判断
3，一个集合是否是一个集合的超集： 调用方法issubset进行判断n
4,两个集合是否没有交集： 调用方法isdisjoint进行判断

集合的数据操作：
1，交集:  &或者使用intersection方法
2，并集:  |或者使用union方法
3，差集:  -或者使用difference
3，对称差集: ^或者使用symmertric_difference方法

集合生成式：
{ i*i for i in range(1,10) }
1，i*i表示集合元素的表达式
2,i是自定义遍历
3,range(1,10)是可迭代对象


"""

#集合生成式
s={ it for it in 'Python'}
print(s)

#集合之间的数学计算
#s={10,20,40}
#s1={10,20,30,40}
#s2={10,20,40}
#s3={1,2,3}
#print(s&s1)
#print(s|s1)
#print(s1-s)
#print(s^s1)


#集合之间的判断
#s={10,20,40}
#s1={10,20,30,40}
#s2={10,20,40}
#s3={1,2,3}
#print(s==s1,id(s))
#print(s==s2,id(s2))
#print(s.issubset(s2))
#print(s.issubset(s1))
#print(s1.issubset(s))
#print(s.isdisjoint(s1))
#print(s.isdisjoint(s3))




#集合的判断操作
#s={1,23,4,5,34}
#s2={11,22,33}
#print(1 in s)
#s.add(79)
#s.update(s2)
#s.update('Python')
#s.remove(79)
##s.remove('w')
#s.discard('w')
#i=8
#for _ in range(i):
#    s.pop()
#print(s)
#s.clear()
#print(s)



#使用{}创建集合
#s2={range(1,4)}
#print(s2,type(s2))
#s={1,2,3,4,5,6}
#print(s,type(s))
#s1=set(range(1,10))
#print(s1,type(s1))

#使用set()创建集合，并且将列表，字符串等可迭代对象转换为集合元素，转换后自动去除重复元素，并且是无序集合
#sq=set([1,23,4,5,5,6])
#print(sq,type(sq))
#sw=set('Pythonnn')
#print(sw,type(sw))
#print(set((2,3,45,6,5,6,6)))





#t=tuple(('hel','jaxc',32))
#for item in t:
#    print(item)

#元组设计成不可变序列的原因
#t=(10,[20,30],9)
#print(t,type(t))
#print(t[0],type(t[0]),id(t[0]))
#print(t[1],type(t[1]),id(t[1]))
#print(t[2],type(t[2]),id(t[2]))
##t[1]=100 #会报错，因为是不可变的序列
#t[1].append(100) #虽然t是元组类型不可变，但是t[1]是列表，列表本身是可变对象,虽然不能修改元组中的元素，但是可以修改元组中列表的元素的内容
#print(t,id(t[1]))

#使用（）创建元组
#t=('Python','hello',90)
#print(t,type(t))
##使用内置函数tuple()创建元组
#t1=tuple(('hell0','sfs',23))
#print(t1,type(t1))
##只包含一个元组的元素需要使用逗号和小括号
#t3=(5,)  #如果括号内不加逗号，则会认为5是int类型
#print(t3,type(t3))
#t4=(2)
#print(t4,type(t4))