s='伟大的中国梦'
#默认编码格式为utf-8，中文占3字节，英文占1字节
scode=s.encode('UTF-8',errors='strict')
print(scode)

#编码格式gbk,中文占2字节，英文占1字节
scode_gbk=s.encode('GBK',errors='strict')
print(scode_gbk)
scode_gbk=s.encode('GBK',errors='replace')
print(scode_gbk)
scode_gbk=s.encode('GBK',errors='ignore')
print(scode_gbk)


#解码
print(bytes.decode(scode_gbk,'GBK',errors='strict'))
print(bytes.decode(scode,'UTF-8',errors='replace'))