#for循环遍历
for i in 'hello':
    print(i)

print('-'*40)

#range()内置函数，用于从[n,m),包含n,不包含m
for i in range (1,11):
    #print(i)
    if i % 2 == 0:
        print(i,'是偶数')

print('-'*40)

#计算1-10之间的累加和
s=0
for i in range (1,11):
    s+=i
print('1-10之间的累加和为:',s)

print('-'*40)

#计算100-999之间的水仙花数
for i in range (100,1000):
    a=i%10
    b=i//10%10
    c=i//100
    if a*a*a+b*b*b+c*c*c==i:
        print(i,'是水仙花数')

print('-'*40)

#for~else语句，else是用来判断程序正常执行循环还是中断
s=0
for i in range (1,11):
    s+=i
else:
    print('1-10之间的累加和为:',s)