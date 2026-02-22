#isdigit判断是否为十进制的阿拉伯数字
print('123'.isdigit()) #True
print('一二三'.isdigit()) #False
print('0b1010'.isdigit()) #False
print('ⅣⅣⅣ'.isdigit()) #False
print('-'*40)
#isnumeric判断所有字符都是数字
print('123'.isnumeric()) #True
print('一二三'.isnumeric()) #True
print('0b1010'.isnumeric()) #False
print('ⅣⅣⅣ'.isnumeric()) #True
print('-'*40)
#isalpha判断所有字符都是数字或字母
print('hello你好'.isalpha()) #True
print('hello你好123'.isalpha()) #False
print('hello你好一二三'.isalpha()) #True
print('hello你好ⅣⅣⅣ'.isalpha()) #False
print('-'*40)
#islower,isupper判断字符的大小写
print('HelloWorld'.islower()) #False
print('helloworld'.islower()) #True
print('hello你好'.islower()) #True
print('HelloWorld'.isupper()) #False
print('HELLO你好'.isupper()) #True
print('HELLOWORLD'.isupper()) #True
print('-'*40)
#istitle判断所有字符都是首字母大写
print('Hello'.istitle()) #True
print('HelloWorld'.istitle()) #False
print('Helloworld'.istitle()) #True
print('Hello World'.istitle()) #True
print('Hello world'.istitle()) #False
print('-'*40)
#isspace判断是否都是空白字符
print('\t'.isspace()) #True
print(' '.isspace()) #True
print('\n'.isspace()) #True