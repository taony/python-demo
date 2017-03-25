# -*- encoding:utf-8 -*-
# !/usr/bin/python3

'''
1、函数的定义

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，
比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

2、定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

def 函数名（参数列表）:
    函数体


'''


def getArea(w, h):
    return w * h;


print(getArea(10, 20));

'''
3、按值传递参数和按引用传递参数
在 Python 中，所有参数（变量）都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如

'''

mylist = [1, 2, 3, 4]


def append_list(mylist):
    mylist.append([0, 1, 2, 3, 4]);
    print("执行函数之后的参数mylist：", mylist);
    return;


append_list(mylist);

print("执行函数之前的参数mylist：", mylist);

'''
4、参数
以下是调用函数时可使用的正式参数类型：必需参数、关键字参数、默认参数、不定长参数

4.1、必需参数
必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
'''

'''
4.2、关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
'''

'''
4.3、默认参数
调用函数时，如果没有传递参数，则会使用默认参数。
'''
def print_age(name="匿名", age=0):
    print(name, ":", age);

# 全参数调用
print_age(age=20);

print_age(name="张三", age=30);

'''
4.4、不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''
def print_mutl_args(defArg,*args):
    print("第一个参数：",defArg);

    print("可变长参数：");

    for x in args:
        print(x,end=",");

# 第一次调用
print_mutl_args(10);

print_mutl_args(1,2,3,4,5,6,"a","b");

'''
5、匿名函数
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
'''

sum=lambda a,b:a+b;

print(sum("lambda:c","d"));

