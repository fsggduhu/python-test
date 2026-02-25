#实战一:提取字符串中所有的数字
def get_digit(x):
    s=0 #存储累加和
    lst=[] #存储提取出来的数字
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    #求和
    s=sum(lst)
    return lst,s

#准备函数的调用
s=input('请输入一个字符串:')
#调用
lst,x=get_digit(s)
print('提取的数字列表为:',lst)
print('累加和为:',x)


print('-'*40)


#实战二:字符串中大小写字母转换
def lower_upper(x):
    lst1=[]
    for item1 in x:
        if 'A'<=item1<='Z':
            lst1.append(chr(ord(item1)+32))
        elif 'a'<=item1<='z':
            lst1.append(chr(ord(item1)-32))
        else:
            lst1.append(item1)
    return ''.join(lst1)

#准备调用
s=input('请输入一个字符串:')
new_s=lower_upper(s)
print(new_s)


print('-'*40)


#实战三:实现操作符in的判断功能
def get_find(s,lst):
    for item in lst:
        if s==item:
            return True
    return False

#准备调用
lst=['hello','world','python']
s=input('请输入你要判断的字符串:')
result=get_find(s,lst)
print('存在' if result else '不存在')