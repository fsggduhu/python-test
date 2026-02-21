#大小写转换
s1='HelloWorld'
new_s2=s1.upper()
print(s1,new_s2)
new_s2=s1.lower()
print(s1,new_s2)

#字符串的分割
e_mail='ysj@126.com'
lst=e_mail.split('@')
print('邮箱名:',lst[0],'邮件服务器域名:',lst[1])


print(s1.count('o'))
print(s1.index('o'))
#print(s1.index('p'))
print(s1.find('p'))
print(s1.find('o'))

#前缀和后缀
print('demo.py'.endswith('.py'))
print(s1.startswith('H'))
print(s1.startswith('P'))

print('-'*40)

mew_s=s1.replace('o','你好',1)#最后一个参数表示替换几次
print(mew_s)

#字符串在指定的宽度范围内居中
print(s1.center(20))
print(s1.center(20,'*'))

#去掉字符串左右的空格
s='    Hello    World    '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#去掉指定的字符
s6='dl-helloworld'
print(s6.strip('ld'))#与顺序无关
print(s6.lstrip('ld'))
print(s6.rstrip('ld'))