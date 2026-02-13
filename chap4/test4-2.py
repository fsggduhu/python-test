#if语句  通过比较运算符计算出来的，结果是布尔类型
number=eval(input('请输入您的6位中奖号码:'))
if number==654321:
    print('恭喜您，中奖了!')

if number!=654321:
    print('抱歉，您未中奖!')

#通过变量运用if语句
n=98
if not n%2:
    print(n,'是偶数') #98%2=0，False,not False为True

print('-------------------判断一个字符串是否是空字符串---------------')
x=input('请输入一个字符串:')
if x:
    print('x是一个非空字符串')

if not x:
    print('x是一个空字符串')

print('----------------表达式也可以是一个单纯的布尔型变量---------------')
flag=eval(input('请输入布尔值:True或False'))
if flag:
    print('该布尔类型为True')

if not flag:
    print('该布尔类型为False')

print('------------使用if语句时，如果语句块中只有一句代码，可以将语句块直接写在冒号的后面------------')
a=10
b=5
if a>b:max=a
print('a和b的最大值为:',max)

'''
if-else语法
if a>b:
    print('最大值为a')
else:
    print('最大值为b')
'''

#if-elif-else
score=eval(input('请输入您的成绩:'))
if score<0 or score>100:
    print('成绩有误!')
elif 0<= score <60:
    print('E')
elif 60<= score <70:
    print('D')
elif 70<= score <80:
    print('C')
elif 80 <=score <90:
    print('B')
else:
    print('A')