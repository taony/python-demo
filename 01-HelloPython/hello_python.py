# -*- coding: utf-8 -*-
#!/usr/bin/python3

print('Hello,Python!');

# 多行注释
'''
单引号多行注释
单引号多行注释
单引号多行注释
'''

"""
双引号多行注释
双引号多行注释
双引号多行注释
"""

# 赋值语句

a=b=c=1;

print (a + b + c)

item_one, item_two, item_three = 1, 2, 3;

# 多行语句

total = item_one +\
        item_two + \
        item_three;

print(total);

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

print(total);

# 同一行显示多条语句

import sys; x = 'runoob'; sys.stdout.write(x + '\n')
