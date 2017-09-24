#!/usr/bin/python

class Student(object):
    def __init__(self,name,age): # __init__()之所以称为构造函数是因为 创建一个类，添加这个类共有的属性,在类生产对象，要想获得这个对象中的属性(数据)则可以添加在self上 通过self.name 
        self.name = name
        self.age = age
        print(type(self))
    def sex(one): #方法函数中必须要有一个参数,否则下面的zhou.sex()无法运行
        
#        self.sex = 'male'
        print('female')

        print(type(self))
        
zhou = Student('zhou xiao hong', 9)
print(zhou.name)
print(zhou.age)
zhou.sex()
#zhou.sex('female')
#print(zhou.sex())
#print(zhou.sex)  #调用sex 方法函数后不() 会打印sex()函数的地址

xia = Student('zhenghua',34)

xia.shenggao = 178
print(xia.shenggao)


class Teacher(object):
    def __init__(self):

