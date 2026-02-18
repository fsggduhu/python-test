#1.使用lst[]直接创建列表
lst=['hello','world']
print(lst)

#2.使用list()创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)
print(lst+lst2)
print('lst'*3)
print(lst2.count('o'))
print(lst2.index('o'))
print(max(lst3))
print(min(lst3))

#列表的删除
lst4=[10,20,30,40,50]
print(lst4)
del lst4[3]
del lst4[0]
print(lst4)

print('-'*40)

#使用for循环遍历列表元素
for item in lst:
    print(item)

#使用for循环，range()函数，len()函数，索引进行遍历
for i in range(0,len(lst)):
    print(i,lst[i])

#使用枚举enumerate()函数
for index,item in enumerate(lst):
    print(index,item) #index是序号，自己也可以手动修改

for index,item in enumerate(lst,start=1): #start可以不写
    print(index,item)

for index,item in enumerate(lst,1):
    print(index,item)