def fun(n):
    if n==1 or n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)
for i in range(1,10):
    print(fun(i),end='\t')
print()