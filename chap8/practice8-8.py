import random
lst=[random.randint(1,100) for i in range(10)]
print(lst)
def get_max(lst):
    x=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>x:
            x=lst[i]
    return x



#计算列表元素的最大值
max=get_max(lst)
print(max)