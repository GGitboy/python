#!/usr/bin/python3

class Student(object):
    def __init__(self,name,score):
        self.__name = name  # 将name 属性私有化 告诉外部使用者不可以直接使用此属性
        self.__score = score # 私有化的属性的方法是在属性前添加2个下划线 
    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))
    def get_name(self):  # 如果要让外部获取name 和 score 定义一个方法 
        return self.__name
    def get_score(self):
        return self.__score
bart = Student('Bart Simpson',98)
bart.score = 59  # 验证 修改私有属性
bart.print_score()
#print(bart.__name)
print(bart.get_name())
print(bart.get_score())



