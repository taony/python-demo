# -*- encoding:utf-8 -*-

# 1、基本的循环方式
a, b = 0, 1
while b < 1000:
    print(b);
    a, b = b, a + b;


# 2、循环跳出
count=0;
while count<=5:
    print(count);
    count+=1;
else:
    print ("count，大于5了");

# 3、