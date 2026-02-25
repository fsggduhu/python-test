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

#根据‘图纸’创建出N多个对象
stu=Student('ysj',18)
stu2=Student('马冬梅',18)
stu3=Student('张三',20)
stu4=Student('王五',23)

print(type(stu))
print(type(stu2))
print(type(stu3))
print(type(stu4))

Student.school=('python教育')

#将学生对象存储到列表中
lst=[stu,stu2,stu3,stu4]
for item in lst:
    item.show()