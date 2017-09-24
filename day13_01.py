#!/usr/bin/python
#-*- coding:utf-8 -*-
#author:suancaiyu

# enumerate 函数将一个可遍列的数据对象组合为一个索引序列，同时列出数据和数据下标。
def main():
    week_overnight = [False,False,Ture,False,False]
    for index,is_overnight in enumerate(week_overnight):
        print ('Today is 星期%d' % (index + 1) )
        try:
            #发生错误怎么处理 
            overnight_check(is_overnight)
        except Exception,e:
            print '发生错误:%s' % (e)
            print '老妈骂了老爸一顿，然后原谅了他'
        else: 
            #没有发生错误的情况 
            print 'append stcripts'
def overnight_check(is_overnight):
    if is_overnight:
        raise Exception('离婚')
    else:
        print '正常'

if __name__=='__main__':
    main()
    
