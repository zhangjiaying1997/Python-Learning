"""
1,封装：提高程序的安全性，
    1）将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。
    2）在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个"_"。
2，继承：提高代码的复用性
    语法格式:
    class 子类类名(父类1，父类2，...):
        pass
    2)如果一个类没有继承任何类，则默认继承object
    3)Python支持多继承
    4）定义子类时，必须在其构造函数中调用父类的构造函数
    5)方法重写：
        ①如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重写编写
        ②子类重写后的方法可以通过super().xxx()调用父类中被重写的方法
    6)object类:
        ①object类是所有类的父类，因此所有类都有object类的属性和方法。
        ②内置函数dir()可以查看指定对象所有属性
        ③object有一个__str__()方法，用于返回一个对于"对象的描述“(即对象的地址），对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对_str_()进行重写
        重写之后将不再使用object类默认输出的对象地址，而是指定的输出内容

3，多态：提高程序的可扩展性和可维护性,即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，
    在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
    1)静态语言和动态语言关于多态的区别
        ①静态语言实现多态的三个必要条件:继承，重写，父类引用指向子类对象
        ②动态语言的多态崇尚'鸭子‘类型，在鸭子类型中，不需要关心对象的类型，只需要关系对象的行为（方法）

4,特殊方法和特殊属性
    1)特殊属性:
        ①__dict__ :获得类对象或实例对象所绑定的所有属性和方法的字典
        ②__class__:
        ③__bases__:
        ④__base__:
        ⑤__mro__:
        ⑥__subclasses__:
    2)特殊方法:
        ①__add__:
        ②__len__:
        ③__init__:
        ④__new__:

5,类的赋值与浅拷贝
    1)变量的赋值：只是形成两个变量，实际上还是指向同一个对象
    2）浅拷贝：Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
    3)深拷贝:使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同



    
"""
#类的浅拷贝
class CPU:
    pass
class DISK:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu1=CPU()
cpu2=cpu1   #变量赋值
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
print('---------浅拷贝首先创建拷贝对象----------')
disk=DISK() #创建一个DISK类对象
computer=Computer(cpu1,disk) #创建一个Computer类对象
print('---------浅拷贝-------------------')
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#深拷贝
print('----------------深拷贝-------------------')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)








#特殊属性
#class A:
#    pass
#class B:
#    pass
#class C(A,B):
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#class D(A):
#    pass
#x=C('Jack',20)  #x是C类的一个实例对象
#print(x.__dict__)   #实例对象的属性字典
#print(C.__dict__)   #类对象和实例对象的__dict__不同，类对象看见的是属性和方法的字典，而实例对象看见的只是属性的字典
#print(x.__class__)  #输出了对象所属的类
#print(C.__bases__)  #输出对象所属父类的一个元组
#print(C.__base__)   #查看类的基类，输出离它最近的父类，即括号里从左往右第一个父类
#print(C.__mro__)    #查看类的层次结构
#print(A.__subclasses__()) #查看当前类的子类列表

#特殊方法
#a=20
#b=100
#c=a+b
#d=a.__add__(b)
#print(c)
#print(d)
#
#class Student:
#    def __init__(self,name):
#        self.name=name
#    def __add__(self,other):
#        return self.name+other.name
##    def __len__(self):
##        return len(self.name)
#
#stu1=Student('张三3')
#stu2=Student('李四')
#s=stu1+stu2 #如果要让两个对象相加就需要编写__add__方法，使得两个对象可以相加
#s=stu1.__add__(stu2)
#print(s)
#lst=[11,22,33,44]
#print(len(lst))
#print(lst.__len__())
#print(stu1.__len__())   #注意必须要重写len方法才可使用

#__init__和__new__创建对象
#class Person(object):
#    def __init__(self,name,age):
#        print('__init__被调用了，self的id值为:{0}'.format(id(self)))
#        self.name=name
#        self.age=age
#    def __new__(cls,*args,**kwargs):
#        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
#        obj=super().__new__(cls)
#        print('创建的对象的id为:{0}'.format(id(obj)))
#        return obj
#
#print('object这个类对象的id为:{0}'.format(id(object)))
#print('Person这个类对象的id为:{0}'.format(id(Person)))
#
#print('--------------------')
#p1=Person('zhangsan',20)
#print('p1这个Person类的实例对象id为:{0}'.format(id(p1)))



#多态
#class Animal(object):   #定义object子类Animal
#    def eat(self):
#        print('动物会吃')
#
#class Dog(Animal):  #定义Animal子类Dog
#    def eat(self):
#        print('狗会吃骨头')
#
#class Cat(Animal):  #定义Animal子类Cat
#    def eat(self):
#        print('猫吃鱼')
#
#class Person(object):   #定义object子类Person
#    def eat(self):
#        print('人吃五谷')
#
#def fun(obj):   #定义一个函数
#    obj.eat()
#fun(Dog())
#fun(Cat())
#fun(Animal())
#print('-------------------------')
#fun(Person())




#继承及其实现方式
#class Person(object):   #Person继承了object类，也可以省略object不写
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def info(self):
#        print(self.name,self.age)
#
#class Student(Person):
#    def __init__(self,name,age,stu_no):
#        super().__init__(name,age)
#        self.stu_no=stu_no
#
#class Teacher(Person):
#    def __init__(self,name,age,teachofyear):
#        super().__init__(name,age)
#        self.teachofyear=teachofyear
#
#stu=Student('张三',20,'1001')
#teacher=Teacher('李四',34,10)
#stu.info()
#teacher.info()
##多继承
#class a:
#    pass
#class b:
#    pass
#class c(a,b)    #c继承于a和b，所以叫做多继承
#    pass
#方法重写
#class Person(object):
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def info(self):
#        print(self.name,self.age)
#
#class Student(Person):
#    def __init__(self,name,age,stu_no):
#        super().__init__(name,age)
#        self.stu_no=stu_no
#    def info(self):
#        super().info()
#        print(self.stu_no)
#class Teacher(Person):
#    def __init__(self,name,age,teachofyear):
#        super().__init__(name,age)
#        self.teachofyear=teachofyear
#    def info(self):
#        super().info()
#        print(self.teachofyear)
#
#stu=Student('zhangsan',20,1001)
#th=Teacher('lisi',35,10)
#stu.info()
#th.info()

#object类
#class Student:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def __str__(self):
#        return '我的名字是{0},今年{1}岁'.format(self.name,self.age)
#stu=Student('zhansan',20)
#print(dir(stu))
#print(stu)  #会默认调用__str__()这样的的方法，所以返回的是定义后的__str__()方法
#print(stu.__str__())
#print(type(stu))


#封装后的私有数据不可以在类的外部访问
#class Car:
#    def __init__(self,brand):
#        self.brand=brand
#    def start(self):
#        print('汽车已启动')
#car=Car('宝马')
#car.start()
#print(car.brand)
