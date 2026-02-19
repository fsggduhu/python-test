lst=['hello','world','python']
print(lst,id(lst))

#在lst最后增加一个元素
lst.append('love')
print(lst,id(lst))
#找出下标为1的元素并增加一个新元素在后边
lst.insert(1,'practice')
print(lst,id(lst))
#清除列表所有元素
# lst.clear()
# print(lst,id(lst))
#将列表中下表为index的元素去除后删除
lst.pop(1)
print(lst,id(lst))
#将列表中的元素反转
lst.reverse()
print(lst,id(lst))
#将列表中下表为index的元素移除
lst.remove('love')
print(lst,id(lst))
#拷贝一个新的列表并打印
new_lst=(lst.copy())
print(lst,id(lst))
print(new_lst,id(new_lst))
#列表元素的修改
lst[1]='hello'
print(lst,id(lst))

