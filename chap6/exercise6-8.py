#findall
import re
pattern='\d\.\d+'
s='I study 3.11 python 2.7 hello'
s2='4.10 python I study'
s3='python I study every day'
lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)
print(lst)
print(lst2)
print(lst3)

#sub
pattern='破解|黑客|反爬'
s='我想破解python,解锁一些vip视频，python可以实现反爬吗'
new_s=re.sub(pattern,'?',s)
print(new_s)

#split
s4='huywefihdwh?bduhew&ghduoiwegf'
pattern='[?|&]'
lst4=re.split(pattern,s4)
print(lst4)