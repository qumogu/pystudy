
"""
1、eval函数的使用，可以让直接执行输入的代码
2、可以把字符的内容，直接转化成list，tuple,disc

3、在开发中，要慎用eval接收input的输入信息，可以直接执行python的代码，时候轻易的执行系统操作
例如 __import__('os').system('rm')，可以删除系统文件
eval中只能import模块的最上一层，例如os要用括号('os')，后面的一级括号进来就会报错
例如__import__('qmg_animal.ani_cat').say_hello() 就会报错，
正确输入：__import__('qmg_animal').ani_cat.say_hello(),就可以了
"""

def main():

    str_data = "['11','22','33','44']"
    print(type(eval(str_data)))

    str_data = "('jack',133,'dog')"
    print(type(eval(str_data)))

    str_data = "{'name':'jack', 'weight':133, '宠物':'dog'}"
    print(type(eval(str_data)))
    
    #return


    while True:
        msg = input("输入命令：")
        if msg == "exit":
            break
        try:
            print(eval(msg))
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    main()