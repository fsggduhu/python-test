#迭代器操作函数
lst=[45,32,66,88]
#(1)排序操作
asc_lst=sorted(lst) #升序
desc_lst=sorted(lst,reverse=True) #降序
print('原列表:',lst)
print('升序:',asc_lst)
print('降序:',desc_lst)

#(2)reversed反向
new_lst=reversed(lst)
print(type(new_lst)) #<class 'list_reverseiterator'>迭代器
print(list(new_lst))

#(3)zip
x=['a','b','c']
y=['10','20','30','40']
zipobj=zip(x,y)
print(type(zipobj))#<class 'zip'>
#print(list(zipobj))

#(4)enumerate
enum=enumerate(y,start=1)
print(type(enum))#<class 'enumerate'>
print(tuple(enum))

#(5)all
lst2=['10','','30','40']
print(all(lst2))#False,必须全为真才输出True
print(all(lst))#True

#(6)any
print(any(lst2))

#(7)
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))


def fun(num):
    return num%2==1
obj=filter(fun,range(10))
print(list(obj))

def upper(x):
    return x.upper()

new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)
print(list(obj2))
