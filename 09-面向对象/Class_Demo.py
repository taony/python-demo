# -*-encoding:utf-8-*-

class Person:
    name = "张三"
    sex = "男"
    def __init__(self):
        self.name="zhangsan";
        self.sex="nv";

    def say(self):
        print("我的名字是：",self.name);


per = Person();

print(per.name);

print(per.sex);

per.say();
