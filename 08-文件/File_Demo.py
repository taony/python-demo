# -*-encoding:utf-8-*-

f = open("file.txt","w");
print("文件名为: ", f.name);

for x in range(1,10):
    f.write(x);

f.write("Hello World");
f.write("\n")


'''
1、fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。
'''
print("fileno：",f.fileno());

#刷新缓冲区
'''
2、flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
'''
f.flush();


'''
3、isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。
'''

# 关闭文件
f.close();

