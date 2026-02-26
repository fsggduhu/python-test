#实战一:计算圆的面积和周长
class Circle:
    def __init__(self,r):
        self.r=r

    #计算圆的面积
    def get_area(self):
        return self.r*3.14*self.r

    #计算圆的周长
    def get_perimeter(self):
        return self.r*3.14*2

r=eval(input("请输入圆的半径:"))
c=Circle(r)
print('圆的面积为:',c.get_area())
print('圆的周长为:',c.get_perimeter())


print('-'*50)


#实战二:定义学生类录入5个学生信息
class Student:
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score

    def info(self):
        print(self.name,self.age,self.gender,self.score)

print('请输入5位学生信息:(姓名#年龄#性别#成绩)')
lst=[]
for i in range(1,6):
    s=input(f'请输入第{i}位学生信息及成绩')
    s_lst=s.split('#')
    #创建学生对象
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
    #将学生对象添加到列表中
    lst.append(stu)

#遍历列表，调用学生对象的info方法
for item in lst:
    item.info()
