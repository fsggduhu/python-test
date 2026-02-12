#赋值运算顺序  从右往左
name='张三'
age=20
a=b=c=d=100 #链式赋值
a,b,c,d='room'
print(a)
print(b)
print(c)
print(d)
print('------输入输出也是顺序结构------')
name1=input('请输入您的姓名:')
age1=eval(input('请输入您的年龄:'))
luck_number1=eval(input('请输入您的幸运数字:'))
print('姓名:',name1)
print('年龄:',age1)
print('幸运数字:',luck_number1)
