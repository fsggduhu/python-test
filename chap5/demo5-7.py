#(1)创建字典
d={10:'a',20:'b',30:'c',20:'d'}
print(d)

#(2)zip函数字典创建
lst1=[23,48,56,89]
lst2=['cat','dog','mouse','rabbit']
zipobj=zip(lst1,lst2)
print(zipobj)
#print(list(zipobj))
d=dict(zipobj)
print(d)

#使用参数创建字典
d=dict(cat=10,dog=20,rabbit=30)
print(d)

#t为key,10为value
t=(10,20,30)
print({t:10}) #使用元组作为字典中的key

#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))
#字典的删除
del d

d1={'hello':10,'world':20,'python':30}
#访问字典中的元素
#(1)使用d[key]
print(d1['hello'])
#(2)使用d.get(key)
print(d1.get('hello'))

#字典的遍历
for item in d1.items():
    print(item)

#在使用for循环遍历时,分别获取key,value
for key,value in d1.items():
    print(key,value)