#实战1
num=input('请输入一个四位整数:') #num=eval(input('请输入一个四位整数:'))
num=int(num)
num1=num%10
num2=num//10%10
num3=num//100%10
num4=num//1000
print('个位上的数字为:',num1)
print('十位上的数字为:',num2)
print('百位上的数字为:',num3)
print('千位上的数字为:',num4)


#用索引
print('-'*40)
num=input('请输入一个四位整数:')
print('个位上的数字为:',num[3])
print('十位上的数字为:',num[2])
print('百位上的数字为:',num[1])
print('千位上的数字为:',num[0])


#实战2
print('-'*40)
height1=eval(input('请输入爸爸的身高:'))
height2=eval(input('请输入妈妈的身高:'))
height3=(height1+height2)*0.54
print('预测儿子的身高为:',round(height3,2))
