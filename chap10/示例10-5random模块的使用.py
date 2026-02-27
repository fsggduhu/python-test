import random
#设置随机数的种子
random.seed(10)
print(random.random()) #[0.0,1.0)
print(random.random())
print('-'*40)
random.seed(10)
print(random.randint(1,100)) #[1,100]

for i in range(10): #[m,n)
    print(random.randrange(1,10,3))

print(random.uniform(1,100)) #[a,b]随机小数

lst=[i for i in range(1,11)]

print(random.choice(lst))

random.shuffle(lst)
print(lst)