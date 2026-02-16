for i in 'hello':
    if i=='e':
        break
    print(i)

print('-------------------------------------------------')

for i in range(3):
    user_name = input('请输入用户名:')
    password = input('请输入密码:')
    if user_name == 'li' and password == '123456':
        print('系统正在登陆，请稍后')
        break
    else:
        if i < 2:
            print('输入错误，你还有', 2 - i, '次机会')
else:
    print('三次输入均错误')