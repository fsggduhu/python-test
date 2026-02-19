#1.对数字的排序
lst=[4,33,98,76,32,45,67]
print('原列表:',lst)

lst.sort()
print('升序:',lst)

lst.sort(reverse=True)
print('降序:',lst)

print('-'*40)

#2.对英文的排序，利用ASCII码值
lst2=['apple','banana','mango','Dog']
lst2.sort()
print('升序:',lst2)

lst2.sort(reverse=True)
print('降序:',lst2)

print('-'*40)

#3.忽略大小写进行排序
lst2.sort(key=str.lower)
print(lst2)

print('-'*40)

#4.使用内置函数sorted()进行排序
#字符串，忽略大小写
inc_lst2=sorted(lst2,key=str.lower)
print('升序:',inc_lst2)
dec_lst2=sorted(lst2,key=str.lower,reverse=True)
print('降序:',dec_lst2)

print('-'*40)

#数字排序
inc_lst=sorted(lst)
print('升序:',inc_lst)
dec_lst=sorted(lst,reverse=True)
print('降序:',dec_lst)
