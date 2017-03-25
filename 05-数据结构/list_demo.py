# -*- encoding:utf-8 -*-
# !/usr/bin/python3

'''
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
以下是 Python 中列表的方法：
'''

#1、list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list1=[1,2,3,4,5];

list1.append(6)

print(list1);

#2、list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list2=[0,1,2,3,4]
list2.extend(list1);
print ('list.extend:',list2);

#3、list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
# 例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list3=["a","b","c"]
list3.insert(0,"d");
print("list.insert:",list3);