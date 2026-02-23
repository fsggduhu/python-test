import re
pattern='\d\.\d+'
s='I study 3.11 python'
match=re.match(pattern,s)
print(match)
s2='3.11 python I study every day'
match2=re.match(pattern,s2)
print(match2)

print('匹配值的起始位置:',match2.start())
print('匹配值的结束位置:',match2.end())
print('待匹配的字符串:',match2.string)
print('匹配的数据:',match2.group())