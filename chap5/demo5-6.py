# #元组的创建与删除
# t=('hello','world',[10,20,30])
# print(t)
#
# #使用内置函数tuple创建元组
# t1=tuple('helloworld')
# print(t1)
#
# t=tuple([10,20,30])
# print(t)
#
# print('10在元组中是否存在:',(10 in t))
# print('10在元组中不存在:',(10 not in t))
# print('最大值:',max(t))
# print('最小值:',min(t))
# print('len:',len(t))
# print('t.index:',t.index(10))
# print('t.count:',t.count(10))
# #元组中只有一个元素
# t=(10,)
# print(t,type(t))
# #元组的删除
# del t

print('-'*40)
#元组的遍历与访问
t=('python','hello','world')
#根据索引访问元素
print(t[0])
#元组的切片
t2=t[0:3:2]
print(t2)

#元组的遍历
for item in t:
    print(item)

for i in range(len(t)):
    print(i,t[i])

#使用枚举
for index,item in enumerate(t,start=11):
    print(index,item)

#元组生成式
t=(i for i in range(1,4))
print(t)
# t=tuple(t)
# print(t)

#遍历
# for item in t:
#     print(item)
#将元组生成器中的元素取出
print(t.__next__())
print(t.__next__())
print(t.__next__())



