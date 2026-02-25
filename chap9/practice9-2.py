class Student:
    #类属性:定义在类中，方法外的变量
    school='北京XX教育'
    #初始化方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

        #定义在类中的函数称为方法，自带一个参数self
    def show(self):
        print(f'我叫:{self.name},今年:{self.age}')

#创建两个Student类型的对象
stu=Student('ysj',18)
stu2=Student('陈梅梅',20)

print(stu.name,stu.age)
print(stu2.name,stu2.age)

#为stu2动态绑定一个实例属性
stu2.gender='男'
print(stu2.name,stu2.gender)
#print(stu.name,stu.gender)


#动态绑定方法
def introduce():
    print('我是一个普通的函数,我被动态绑定成了stu2对象的方法')
stu2.func=introduce
#调用
stu2.func()