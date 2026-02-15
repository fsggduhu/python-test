#使用while循环模拟用户登录
#(1)初始化变量
i=0
while i<3:
    user_name=input("enter your name:")
    password=input("enter your password:")
    if user_name=='li' and password=='666666':
        print("登录成功")
        i=8#目的是改变变量，跳出循环
    else:
        if i<2:
            print("用户名或密码不正确，你还有",2-i,'次机会')
        i+=1
if i==3:
    print("抱歉，三次输入的均不正确，机会已用完")
