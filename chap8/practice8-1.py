#个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

#调用
fun(10,20,30,40)
fun(10)
fun(20,30)
fun([11,22,33,44]) #实际上传递的是一个参数
#在调用时，参数前加一颗星会将列表进行解包
fun(*[11,22,33,44])

print('-'*30)

#个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,value)

#调用
fun2(name='李',age=18,heiget=170)

d={'name':'李','age':18,'heiget':170}
fun2(**d)#参数是字典必须加**