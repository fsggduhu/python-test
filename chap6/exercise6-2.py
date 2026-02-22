#使用占位符进行格式化输出
name='马冬梅'
age=18
score=98.5
print('姓名:%s,年龄:%d,成绩:%.1f' % (name,age,score))


#f-string进行格式化输出
print(f'姓名:{name},年龄:{age},成绩:{score}')


#使用字符串的format方法
print('姓名:{0},年龄:{1},成绩:{2}'.format(name,age,score))
print('姓名:{2},年龄:{0},成绩:{1}'.format(age,score,name))

print('-'*40)


#format详细格式控制
s='helloworld'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))#居中
#居中对齐
print(s.center(20,'*'))

#千位分隔符(只适用于整数和浮点数)
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.9876))

#浮点数小数部分的精度
print('{0:.2f}'.format(9.98765431))
#字符串类型.表示是最大的显示长度
print('{0:.5}'.format('helloworld'))
#整数类型
a=673
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制:{0:X}'.format(a))
#浮点数类型
b=9.87654321
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))