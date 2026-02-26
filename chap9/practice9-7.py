class Person():
    def eat(self):
        print('人,吃五谷杂粮')

class Cat():
    def eat(self):
        print('猫,吃小鱼🐟')

class Dog():
    def eat(self):
        print('狗,喜欢啃骨头')

def fun(obj):
    obj.eat()

#创建三个类的对象
per=Person()
cat=Cat()
dog=Dog()

#调用fun函数
fun(per)
fun(cat)
fun(dog)