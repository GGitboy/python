#!/usr/bin/python
#-*- coding:utf-8 -*- 指定python 使用的编码
#author:suancaiyu  注释

#本次的学习内容有: 思考变量，输出，判断,python编码风格， 编程的思想是什么
#编程实现老妈去去市场买菜，如果价格合理，就买2斤，否则就不买。
#如果商品的价格每下降1元，老妈就多买1斤，最多买4斤

def main():
    who = '老妈'
    goods_description="西双版纳大白菜"

    is_cheap=False

    goods_price=5
    resonable_price=5
    

    print( "%s上街看到%s,卖 %d 元/斤" %(who,goods_description,goods_price))

    if(goods_price<=resonable_price):
        print ('%s认为便宜' %(who))
        is_cheap=True
        buy_amount=2+(resonable_price-goods_price)
        if buy_amount>4:
            buy_amount=4
        print ('她买了%d斤' %(buy_amount))
    else:
        print( '她认为贵了')
        is_cheap=False
        print ('她并没有买，扬长而去')
#函数的入口
if __name__=='__main__':
    main()




