/*
这是一个方便Python程序调用的dll动态库
写了一个死循环，方便测试,解决python的GIL问题
使用如下命令，进行编译成动态库
gcc xxx.c -shared -o libxxxx.so

在01gil04.py中有调用
*/

void DeadLoop()
{
    while(1)
    {
        ;
    }
}
