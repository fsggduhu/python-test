from datetime import datetime
from datetime import timedelta
#创建两个datetime类型的对象
delta1=datetime(2028,10,1)-datetime(2008,8,8)
print('delta1的数据类型是:',type(delta1),'delta1所表示的数据:',delta1)
print('2008年8月8日之后的7359天是:',datetime(2008,8,8)+delta1)

#通过传入参数的方式创建一个timedelta对象
td1=timedelta(8)
print('创建一个8天的timedelta对象',td1)
td2=timedelta(10,11)
print('创建一个10天11秒的timedelta对象',td2)
