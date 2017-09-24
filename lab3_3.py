#!/usr/bin/python

class Animal():
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):   #当子类和父类都有相同的方法时，我们说子类的方法覆盖父类的方法
        print('Dog is running...')  # 在运行方法的时候 总是先调用子类
class Cat(Animal):
    def run(self):
        print('Cat is running...')
    def eat(self):
        print('cat is  eat meat...')
dog = Dog()
dog.run()

cat =Cat()
cat.run()
cat.eat()

a = list()  # a 是list 类型
b = Animal() # b  是animal 类型
c = Dog()  # c 是 dog 类型
# 判断 某个对象是否是某个类型可以用isinstance()判断 
print(isinstance(a,list))
isinstance(b,Animal)  # 判断b是不是Animal 类型
isinstance(c,Dog)   #判断 c是不是Dog类型
isinstance(c,Animal)  # 判断 c 是不是Animal类型 发现c 既是Dog类,也是 Animal类
