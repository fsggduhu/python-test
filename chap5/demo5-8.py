d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)

#向字典中添加元素
d[1004]='张丽丽'
print(d)

#获取字典当中所有key
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

#获取字典中所有的value
values=d.values()
print(values)
print(list(values))
print(tuple(values))

#如何将字典中的数据转成key-value的形式,以元组的方式进行展现
lst=list(d.items())
print(lst)

d=dict(lst)
print(d)

#使用pop函数
print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))

#随机删除
print(d.popitem())
print(d)

#清空字符中的所有元素
d.clear()
print(d)

#python中一切皆对象，每个都有对应的布尔值
print(bool(d))

#字典生成式
import random
#1.
d={item:random.randint(1,100) for item in range(4)}
print(d)
#2.
lst3=[1006,1007,1008,1009]
lst6=['张三','李四','王五']
d={key:value for key,value in zip(lst3,lst6)}
print(d)