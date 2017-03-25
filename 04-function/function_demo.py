# -*- encoding:utf-8 -*-
#!/usr/bin/python3

'''
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

'''


def getArea(w, h):
    return w * h;


print(getArea(10, 20));

'''
按值传递参数和按引用传递参数
在 Python 中，所有参数（变量）都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如

'''

mylist = [1, 2, 3, 4]


def append_list(mylist):
    mylist.append([0, 1, 2, 3, 4]);
    print("执行函数之后的参数mylist：" , mylist);
    return;


append_list(mylist);

print("执行函数之前的参数mylist：" ,mylist);

