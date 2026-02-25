class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    def show(self):
        print(f'我叫{self.name},我的性别是{self.gender}')

#定义两个类
class Student(Person):
    #编写初始化方法
    def __init__(self,name,gender,stuno):
        super().__init__(name,gender)
        self.stuno=stuno

    def show(self):
        super().show()
        print(f'我来自xxx大学，我的学号是:{self.stuno}')

class Docter(Person):
    def __init__(self,name,gender,department):
        super().__init__(name,gender)
        self.department=department


    def show(self):
        # super().show()
        print(f'大家好，我叫:{self.name},我的性别是:{self.gender},我的工作科室是:{self.department}')

#创建第一个子类对象
stu=Student('陈梅梅','女','1001')
stu.show()

docter=Docter('张一一','男','外科')
docter.show()