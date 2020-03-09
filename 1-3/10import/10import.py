"""
导入模块知识点
1、如果模块名步方便书写或阅读，用as 来取别名使用,别名用大驼峰命名法
2、如果导入多个模块中，有同名的函数，最后一个导入的会覆盖前面导入的
3、如果想用多个模块中同名的函数和工具，可以用as的取别名使用
4、导入的文件里面，不要顶格书写语句，否则也会被执行，
5、pyhton中当前执行的文件，有一个内置变量__name__ 会为__main__,通用格式都是，
    if __name__ == "__main__":
        main()
    在main()中做代码测试。
6、导入模块的__file__显示导入模块的文件路径
"""
import 导入测试_模块1 as ModelDog
from 导入测试_模块2 import say_hello
#模块1覆盖模块2的函数
from 导入测试_模块1 import say_hello
from 导入测试_模块2 import say_hello as cat_sayhello
from 导入测试_模块2 import Cat


def main():

    dog = ModelDog.Dog("Jack")
    cat = Cat("Tom")

    print(dog)
    print(ModelDog.__file__)
    say_hello()
    cat_sayhello()
    dog.eat_food("骨头")
    cat.run_speed(15)


if __name__ == "__main__":
    main()