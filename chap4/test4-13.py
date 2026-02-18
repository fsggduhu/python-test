#1.判断是否为闰年
year=eval(input('请输入一个四位的年份:'))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,'年是闰年')
else:
    print(year,'年是平年')

print('-'*30)

#2.模拟10086查询功能
answer='y'
while answer=='y':
    print('-----------欢迎使用10086查询功能-----------')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询当前剩余通话')
    print('0.退出自助系统')
    choice=input('请输入要进行的操作')
    if choice=='1':
        print('当前余额为235元')
    elif choice=='2':
        print('当前剩余流量为2GB')
    elif choice=='3':
        print('当前剩余通话为100分钟')
    elif choice=='0':
        print('程序退出，谢谢您的使用')
        break
    else:
        print('输入无效，请重新输入')
    answer=input('继续执行操作吗?y/n')
else:
    print('退出自助系统')

print('-'*30)

#3.九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(j*i),end=' ')
    print()

print('-'*30)

#4.猜数游戏
import random
rand=random.randint(1,100)
count=1
while count<=10:
    number=eval(input('猜猜我想的数字是:'))
    if number==rand:
        print('恭喜你，猜对了')
        break
    elif number>rand:
        print('猜大了')
    else:
        print('猜小了')
    count+=1
if count<=3:
    print('真聪明，一共猜了',count,'次')
elif count<=6:
    print('还可以,一共',count,'次')
else:
    print('猜的次数有点多啊，一共',count,'次')
