# -*-encoding:utf-8-*-

#一、输出格式美化

'''
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''

hello='hello';

print(str(hello));
print(repr(hello));


#二、填充字符串
'''
rjust:靠右补齐
ljust:靠左补齐
center:居中补齐
'''
print(hello.rjust(20, 'r'));
print(hello.ljust(20, 'l'));
print(hello.center(20, 'c'));

'''
zfill()：会在数字的左边填充 0
'''
print("123".zfill(7));
print("3.14".zfill(5));

#三、str.format()
print("姓名：{}，年龄：{}".format("zhangsan","20"));

print("姓名：{0}，年龄：{1}".format("zhangsan","20"));

print("姓名：{1}，年龄：{0}".format(30,"lisi"));

print("姓名：{name}，年龄：{age}".format(name="wangwu",age="20"));

