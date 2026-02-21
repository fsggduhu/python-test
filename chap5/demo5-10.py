#1.千年虫是什么虫
#方法一:使用range()
lst=[88,89,90,00,99]#表示员工两位整数出生年份
print(lst)
# for index in range(len(lst)):
#     if str(lst[index]) !='0':
#         lst[index]='19'+str(lst[index])#拼接年份再赋值
#     else:
#         lst[index]='200'+str(lst[index])
# print(lst)

#方法二:使用enumerate()
for index,value in enumerate(lst):
    if str(value) !='0':
        lst[index]='19'+str(value)#拼接年份再赋值
    else:
        lst[index]='200'+str(value)
print('输出后的年份:',lst)

print('-'*40)

#2.模拟京东的购物流程
#创建一个空列表，用于存储入库的商品信息
lst=[]
for i in range(5):
    goods=input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品:')
    lst.append(goods)
#输出所有的商品信息
for item in lst:
    print(item)
#创建一个空列表，用于存储购物车中的商品
cart=[]
while True:
    flag=False
    num=input('请输入要购买的商品编号:')
    #遍历商品列表，查询要购买的商品是否存在
    for item in lst:
        if num==item[0:4]:
            flag=True
            cart.append(item)
            print('商品已成功添加到购物车')
            break
    if not flag and num !='q':
        print('商品不存在')
    if num=='q':
        break
print('-'*60)
print('您购物车里选择的商品为:')
cart.reverse()
for item in cart:
    print(item)

print('-'*40)

#3.模拟12306车票订票流程
#创建字典用于存储车票信息，使用车次作key，使用其他信息作value
dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G1568':['北京南-天津西','18:20','18:19','00:59'],
    'G203':['北京南-天津南','18:35','19:09','00:34']
}
print('车次          出发站-到达站     出发时间       到达时间        历时时长')
for key in dict_ticket.keys():
    print(key,end=' ')
    for item in dict_ticket.get(key):
        print(item,end='\t\t')
    print()

#输入用户的购票车次
train_no=input('请输入要购买的车次:')
info=dict_ticket.get(train_no,'车次不存在')
#判断车次是否存在
if info !='车次不存在':
    person=input('请输入乘车人，如果是多位乘车人使用逗号分隔:')
    s=info[0]+' '+info[1]+'开'
    print('您已购买了'+train_no+' '+s+',请'+person+'尽快换取纸质车票')
else:
    print('对不起，选择的车次可能不存在')