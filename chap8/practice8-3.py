def cala(a,b):
    return a+b
print(cala(10,20))

#匿名函数
s=lambda a,b:a+b
print(type(s))
#调用匿名函数
print(s(10,20))

lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print()

for i in range(len(lst)):
    result=lambda x:x[i] #根据索引取值，x是形式参数
    print(result(lst)) #lst是实际参数


print('-'*40)


student_scores=[
    {'name':'陈每每','score':90},
    {'name':'张三','score':80},
    {'name':'李四','score':70},
]
#对列表进行排序
student_scores.sort(key=lambda x:x.get('score'), reverse=True)
print(student_scores)