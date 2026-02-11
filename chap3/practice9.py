s=3.14+3
print(s,type(s))
print(round(s,2))  #保留小数点后两位


#eval()常与input()一起使用
age=eval(input('请输入你的年龄:'))
print(age,type(age))
height=eval(input('请输入你的身高:'))
print(height,type(height))

hello='北京欢迎你'
print(hello,type(hello))
print(eval('hello'))

