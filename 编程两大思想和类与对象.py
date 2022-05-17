"""
1,类与对象
    1）类
    ①创建类的语法：
    class 类名:
        pass
    ②类的组成
    Ⅰ类属性:直接写在类里面的变量，类中方法外的变量称为类属性，被该类的所有对象所共享
    注意：在类之外定义的叫函数，在类之内定义的叫方法
    Ⅱ实例方法:
    def 方法名（self）:
        pass
        注意：一般括号里都是写self,不写自动默认为self
    Ⅲ静态方法
    @staticmethod
    def 方法名():
        pass
        注意：静态方法括号里不能有self
    Ⅳ类方法
    @classmethod
    def 方法名(cls):
        pass
        注意：类方法括号里是cls
    Ⅴ初始化方法
    def __init__(self,name,age):
        self.name=name  #self.name称为实体属性，进行了一个赋值操作，将局部变量的name的值赋给实体属性
        self.age=age
    2)对象的创建(类的实例化)
    语法：
        实例名=类名（）
    注意：类方法的使用：
    ①使用实例对象去使用方法:   stu1.eat() #其中stu1是一个实例对象，调用了stu1所属类Student中的eat方法
    ②使用类方法带实例参数:    Student.eat(stu1) #即将类的实例放在方法参数里
    3)动态绑定属性和方法
    ①动态绑定属性:即在类之外定义一个专属于某个类实例的变量，称为动态绑定属性，这种属性只属于这一个类实例，不属于类对象，其余类实例无法使用
    ②动态绑定方法:即在类之外定义一个函数，再将函数绑定到某个类实例上，即称为该类实例的类方法，该方法不属于类对象，只属于该类实例，其余类实例无法使用
"""
#类的创建(模板)
class Student:  #Student为类名，一般由一个或多个单词组成，每个单词首字母大学，其余小写
    native_pace='记录'    #写在类里面的变量，称为类属性
    def __init__(self,name,age):
        self.name=name  #self.name称为实体属性，进行了一个赋值操作，将局部变量的name值赋给实体属性
        self.age=age
    #实例方法
    def eat(self):
        print('我在学Python')
    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')
#类属性的使用
stu1=Student('zhangsan',20)
stu2=Student('lisi',25)
print(Student.native_pace)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='湖南'
print(stu1.native_pace)
print(stu2.native_pace)
print('-------------------类方法的使用--------------')
Student.cm()
stu1.cm()
stu1.cm()
print('-------------------静态方法的使用-------------')
Student.method()
stu1.method()
stu2.method()
print('-------------动态绑定类属性-------------')
stu1.gender='男'
print(stu1.gender)
#print(stu2.gender) #该类属性gender只属于类stu1,因此stu2使用会报错
print('-------------动态绑定方法---------------')
def a():
    print('我是专属类方法')
stu1.a=a
stu1.a()
#stu2.a() #该类方法a()只属于类stu1,因此，stu2使用会报错




#创建类的实例对象
#stu=Student('Jack',20)
#print(stu.name)
#print(stu.age)
#print(id(stu))
#print(type(stu))
#print(stu)
##使用类创建的对象去使用类方法
#stu1=Student('zh',25)
#stu1.eat()  #方法的两种使用方式
#Student.eat(stu1) #方法的两种使用方式
#print(stu1.age)
#print(stu1.name)


#Python中一切对象Student是对象吗？有分配内存空间吗？
#print(id(Student))  #输出Student对象的地址，即可知道以及分配内存空间
#print(type(Student))    #输出Student对象的类型，即为所创建类的类型
#print(Student)  #输出对象Student的值value