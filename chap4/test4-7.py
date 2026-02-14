#(1)初始化变量
answer=input('今天上课吗')
while answer == 'y': #(2)条件判断
    print('hello,上课') #(3)语句块
    #(4)改变变量
    answer=input('今天上课吗')

#1-100之间的累加和
'''
s=0
i=1
while i<=10:
    s+=i
    i+=1
print('1-10之间的累加和:',s)
'''

print('-'*40)

#while~else语句
s=0
i=1
while i<=10:
    s+=i
    i+=1
else:
    print('1-10之间的累加和:',s)