#!/usr/bin/python
#-*- coding:utf-8 -*-
#author:Suancaiyu
def print_list(lst):
    for item in lst:
        print (item)
def main():
    list=[1,2,3,4,5,a,b,c,d,e,f]
    list2=list[1:]
    print_list(list)
    print_list(list2)
if __name__=='__main()__':
    main()

