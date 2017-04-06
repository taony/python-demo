# -*-encoding:utf-8-*-

#一、输出格式美化

'''
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''

hello='hello';

print(str(hello));
print(repr(hello));


'''
rjust:靠右补齐
ljust:靠左补齐
center:居中补齐
'''
print(hello.rjust(20, 'r'));

print(hello.ljust(20, 'l'));

print(hello.center(20, 'c'));


