import re
pattern='\d\.\d+'
s=('I study 3.11 python 2.7 hello')
match=re.search(pattern,s)
print(match)


s2='4.10 python I study'
s3='python I study every day'
match2=re.search(pattern,s2)
match3=re.search(pattern,s3)
print(match2)
print(match3)
print(match.group())
print(match2.group())