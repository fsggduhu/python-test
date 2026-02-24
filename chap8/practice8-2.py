def calc(a,b):
    s=a+b
    return s

result=calc(1,2)
print(result)


print('-'*40)
m=100

def calc2(x,y):
    return m+x+y
print(m)
print(calc2(1,2))

print('-'*30)

def calc3(x,y):
    n=200
    return n+x+y

print(calc3(1,2))
print('-'*30)

def calc4(x,y):
    global s
    s=300
    return s+x+y
print(calc4(1,2))
print(s)