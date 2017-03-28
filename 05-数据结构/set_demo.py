# -*- encoding:utf-8 -*-
# !/usr/bin/python3

'''
集合
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构。

'''

# 1、声明了集合，但是集合元素输出的时候，会过滤重复元素
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'};
print(basket);

# 2、集合之间的计算
a = set('a,b,c,d');
b = set('a,b,c,e,f');

# 2.1 a - b，在 a 中的字母，但不在 b 中
print(a - b);

# 2.2 a | b ,在 a 或 b 中的字母，并集
print(a | b);

# 2.3 a & b ,在 a 和 b 中都有的字母
print(a & b);

# 2.4 a^b ，在a或者b中，但不同时在a和b中的元素
print(a ^ b);
