#import
import my_info
print(my_info.info())
my_info.info()


import my_info as a
print(a.name)
a.info()

#from...import
from my_info import name #导入的是一个具体的变量的名称
print(name)

from my_info import info #导入的是一个具体的函数的名称
info()

#通配符
from my_info import *
print(name)
info()

#同时导入多个模块
import math,time,random