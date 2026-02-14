answer=input('请问，您喝酒了吗?')
if answer == 'y':
    proof=eval(input('请输入酒精含量:'))
    if proof<20:
        print('构不成酒驾，请您一路平安')
    elif proof<80:
        print('已构成酒驾，请不要开车!')
    else:
        print('已到达醉驾标准')
else:
    print('没喝酒，你走吧')