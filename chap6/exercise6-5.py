s1='hello'
s2='world'

#(1)使用+进行拼接
print(s1+s2)


#(2)使用join()进行拼接
print(''.join([s1,s2])) #使用空字符串进行拼接
print('*'.join(['python','pycharm','hello','world']))
print('你好'.join(['python','pycharm','hello','world']))


#(3)直接拼接
print('hello''world')


#(4)使用格式化字符串进行拼接
print('%s%s' % (s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))


print('-'*40)


#字符串的去重操作
s='hellodasdsdads'
#方法一:字符串拼接+not in
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item
print(new_s)

#方法二:使用索引+not in
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

#方法三:通过集合去重+列表排序
new_s3=set(s)
lst=list(new_s3)
lst.sort(key=s.index)
print(''.join(lst))