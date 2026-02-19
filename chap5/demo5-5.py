import random
#一维列表
lst=[item for item in range(10)]
print(lst)

lst=[item*item for item in range(10)]
print(lst)

lst=[i for i in range(10) if i%2==0]
print(lst)

lst=[random.randint(1,100) for i in range(10)]
print(lst)

print('-'*40)

#二维列表
lst2=[
    ['城市','环比','同比'],
    ['北京',100,101],
    ['上海',102,103],
    ['广州',104,105]
]
print(lst2)

for row in lst2:
    for item in row:
        print(item,end='\t')
    print()

#列表生成式生成四行五列的表格
lst3=[[j for j in range(5)]for i in range(4)]
print(lst3)
