s=0
i=1
while i<11:
    s+=i
    if s>20:
        print('累加和大于20的当前数字是:',i)
        break
    i+=1



print('-'*40)

i=0
while i<3:
    user_name=input('请输入用户名:')
    password=input('请输入密码:')
    if user_name=='li' and password=='123456':
        print('系统正在登陆，请稍后')
        break
    else:
        if i<2:
            print('输入错误，你还有',2-i,'次机会')
    i+=1
else:
    print('三次输入均不正确')