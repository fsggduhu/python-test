import time
now=time.time()
print(now)

obj=time.localtime() #struct_time对象
print(obj)

obj2=time.localtime(60)
print(obj2)
print(type(obj2))
print('年份:',obj2.tm_year)
print('月份:',obj2.tm_mon)
print('日期:',obj2.tm_mday)
print('时:',obj2.tm_hour)
print('分:',obj2.tm_min)
print('秒:',obj2.tm_sec)
print('星期:',obj2.tm_wday) #[0,6],3表示星期四
print('今年的多少天:',obj2.tm_yday)
print(time.ctime()) #时间戳对应的易读字符串

#日期时间格式化
print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.strftime('%H:%M:%S',time.localtime()))
print('%B月份的名称:',time.strftime('%B',time.localtime()))
print('%A月份的名称:',time.strftime('%A',time.localtime()))

#字符串转成struct_time
print(time.strptime('2008-08-08','%Y-%m-%d'))

time.sleep(5)
print('helloworld')