from my_info import *
from introduce import *
#导入模块中具有同名的变量和函数，后倒入的会覆盖前导入的
info()

#如果不想覆盖，使用import
import my_info
import introduce

my_info.info()
introduce.info()