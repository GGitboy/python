#!/usr/bin/python
#-*-coding:utf-8 -*-
#author:suancaiyu


def main():
    car1="捷达"
    speed1 = 60 
    distance1 = 300
    hour = distance1/speed1
    #print "驾驶%s 开 %d km 去太空开了%f 小时" % (car1,distance1,hour)
    print '驾驶 %s 开 %dkm 去b地开了 %0.2f 小时' % (car1, distance1, hour) 
    car2 = "捷豹"
    speed2 = 120
    distance2 = 400
    hour2 = float(distance2)/speed2
    print '驾驶%s 开 %d km 去太空花了%f 小时' % (car2,distance2,hour2)

if __name__=='__main__':
    main()
