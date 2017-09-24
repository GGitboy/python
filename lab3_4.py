#!/usr/bin/python 
#怎样判断一个对象的类型 type()
import types

print(type(123))

print(type('str'))


print(type(None))
print("abs's type is ", type(abs))

# 思考type() 函数返回的是什么类型呢？
print(type(123) == type(345))

print(type(123) == int )
#所以 说type返回的class 类


#判断一个对象是不是函数
def  fn():
    pass
print (type(fn) == types.FunctionType)

# 对于 class 继承关系来说，使用type()是不方便的，可以使用 isinstance()函数 
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass

a = Animal()
b = Dog()
c = Husky()

print(isinstance(c,Husky))
print(isinstance(c,Dog))
print(isinstance(c,Animal))
print(isinstance(b,Husky))

#可以用type()类型判断 的也可以 用isinstance  来判断 


