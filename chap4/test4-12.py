#while语句中的if-continue语句
s=0
i=1
while i<=100:
    if i%2==1:
        #print(i,'为奇数')
        i+=1
        continue
    s+=i
    i+=1
print('偶数项的累加和为:',s)

print('-'*30)

#for语句中的if-continue语句
s=0
for i in range(1,101):
    if i%2==1:
        continue
    s+=i
print('偶数项的累加和为:',s)

print('-'*30)

if True:
    pass

while True:
    pass

for i in range(10):
    pass
