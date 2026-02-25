class Student():
    def __init__(self,name,age,gender):
        self._name=name #受保护的
        self.__age=age #私有的
        self.gender=gender #普通的

    def _fun1(self):
        print('子类及本身可以访问')

    def __fun2(self):
        print('只有定义的类可以访问')

    def show(self):
        self._fun1() #类本身访问受保护的方法
        self.__fun2() #类本身访问私有方法
        print(self._name) #受保护的实例属性
        print(self.__age) #私有的实例属性

#创建一个学生类的对象
stu=Student('陈梅梅',20,'女')
print(stu._name)
#print(stu.__age)

#调用受保护的实例方法
stu._fun1()
#stu.__fun2()

#访问私有
print(stu._Student__age)
stu._Student__fun2()

print(dir(stu))