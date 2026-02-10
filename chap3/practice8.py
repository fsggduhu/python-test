x=10
y=3
z=x/y
print(z,type(z))

#float类型转成int类型，只保留整数部分
print('float转成int类型:',int(3.14))
print('float转成int类型:',int(3.9))
print('float转成int类型:',int(-3.14))
print('float转成int类型:',int(-3.9))


#将int转成float类型
print('int转成float类型:',float(10))

#将str转成int类型
print(int('100')+int('200'))

#chr(),ord()
print(ord('杨')) #杨在unicode表中对应的字符串
print(chr(26643)) #26643在unicode表中对应的字符

#进制之间的转换函数，十进制与其他进制之间的转换
print('十进制转成十六进制:',hex(26643))
print('十进制转成八进制:',oct(26643))
print('十进制转成二进制:',bin(26643))