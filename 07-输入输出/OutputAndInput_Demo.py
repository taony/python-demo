# -*-encoding:utf-8-*-

#一、输出格式美化

'''
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''

hello='hello';

print(str(hello));
print(repr(hello));

print (hello.rjust(10, '0'));


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')