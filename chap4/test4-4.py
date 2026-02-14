#使用and连接多个选择条件
user_name=input('请输入您的用户名:')
password=input('请输入您的密码:')
if user_name=='admin' and password=='123456':
    print('登录成功!')
else:
    print('用户名或密码不正确，请重新输入')



print('-'*40)



#使用or连接多个选择条件
score=eval(input('请输入您的成绩:'))
if score<0 or score>100:
    print('成绩无效!')
else:
    print('您的成绩为:',score)