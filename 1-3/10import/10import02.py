"""
导入模块知识点
1、导入包信息
2、如果修改了包内的.py文件，一定要先保存包文件，在运行主程序，否则会报错
"""
import qmg_animal
from qmg_animal.ani_cat import Cat


def main():

    dog = qmg_animal.ani_dog.Dog("Jack")
    cat = Cat("Tom")

    print(cat)
    print(qmg_animal.__file__)
    qmg_animal.ani_dog.say_hello()
    qmg_animal.ani_cat.say_hello()
    dog.eat_food("骨头")
    cat.run_speed(15)


if __name__ == "__main__":
    main()