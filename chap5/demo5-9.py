s={10,20,30}
print(s)

#集合为不可变数据类型，列表为可变数据类型
# s={[10,20,30],50,80}
# print(s)

#使用内置函数set()创建集合
s=set()
print(s)
s={}
print(s)
print(type(s))

s=set('helloworld')
print(s)

s1=set([10,20,30])
print(s)

s2=set(range(1,10))
print(s2)

print('-'*40)
#集合属于序列中的一种
print('max:',max(s2))
print('min:',min(s2))
print('sum:',sum(s2))
print('len:',len(s))

print('9在集合中存在:',9 in s2)
print('9在集合中不存在:',9 not in s2)

#集合的删除
del s2
#print(s2)

print('-'*40)

A={10,20,30,40,50}
B={90,20,30,66,50}
print(A&B)#交集
print(A|B)#并集
print(A^B)#补集
print(A-B)#差集

print('-'*40)

#集合的相关操作
s6={10,20,30}
#向集合中添加元素
s6.add(66)
print(s6)
#删除集合中的元素
s6.remove(66)
print(s6)
#清空集合中所有元素
# s6.clear()
# print(s6)

#集合的遍历
for item in s6:
    print(item)

for index,item in enumerate(s6):
    print(index,item)

#集合生成式
s7={i for i in range(1,10)}
print(s7)

s7={i for i in range(1,10) if i%2==1}
print(s7)