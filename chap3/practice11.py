x=20 #直接将20赋值给变量x
y=10
x=x+y #将x+y的和赋值给x,x=30
print(x)
x+=y
print(x) #x=40
x-=y
print(x) #x=30
x*=y
print(x) #x=300
x/=y
print(x) #x=30.0
print(type(x))
x%=y
print(x) #x=0.0
z=3
y//=z
print(y) #y=3
y**=2
print(y) #y=9

#Python中的链式赋值
a=b=c=100
print(a,b,c)

#Python支持系列解包赋值
a,b=10,20
print(a,b)

#利用系列解包赋值交换两个变量的值
a,b=b,a
print(a,b)