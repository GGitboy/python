#!/usr/bin/python3
# 类是抽象的模板
class Dog(object):  
    def __init__(self,name): #类需要一个构造方法，python 中__init__是python的构造方法
        self._name = name
#定义一个类的时候也可以不需要__init__ 方法
    def get_name(self):
        return self._name
#    def set_name(self,value):
#        self._name = value
#        pirnt(value)
    def bark(self):
        print(self.get_name() + ' is making sound wang wang wang ...')
dog =Dog('wangcai')
dog.bark()

class Test():
    def prt(self): # self  代表类的实例，而非类,类的实例也就是一个对象
        print(self)
        print(type(self))
        print(self.__class__)
t = Test()
t.prt()


# object 表示该类是从哪个类继承下来的，通常如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    pass
bart = Student() # 每个对象拥有相同的方法，但各自的数据可能不同
bart.name = 'Bart Simpson'  #可以自由的给对象绑定属性
print(bart)
print(Student)
print(bart.name)

# 类是抽象的模板，在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去，通过一个特殊的方法:__init__ ，
#__init__方法的第一个参数永远是self ，表示创建实例对象本身，不需要传递该参数，python解释器自己会实例对象传进去。 
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
#实例变量   
class Teacher(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

one = Teacher('Mary',59) # 创建一个实例
print(one.score)
print(one.name)
#面向对象的一个重要特点就是数据封装，在Teacher类中创建的实例都有name,score这些数据，这里定义一个外部函数来访问这些数据，如下 函数打印name,score
def print_score(argv):
    print('%s:%s' %(argv.name,argv.score))
print_score(one)

#但是实例本身就拥有这些数据，要访问这些数据就没有必要从外面的函数去访问，可以直接从类的内部定义访问数据的函数 ，这样就把“数据”封装起来了。这些封装数据的函数和类本身是关联起来的。在类中称之为方法
class Cat(object):
    def __init__(self,name,weight):  # name ,weight 为参数
        self.name = name
        self.weight = weight
    
    def print_cat(self):
        print('%s:%.3f' %(self.name,self.weight))
cat = Cat('Kitty',2.32)
cat.print_cat()  #方法可以直接在实例变量上调用，不需要知道内部的细节
# 从外部看cat类，只需要知道创建实例给出 name,weight ，而如何打印都是在Cat类中内部定义的，这些数据和逻辑被封装起来了，调用容易又不知内部实现的细节
#封装的另一个好处就是可以给Cat 类增加新的方法，

