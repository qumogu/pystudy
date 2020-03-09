"""
练习制作发布压缩包
步骤
1、编写setup.py
2、在目录下，使用python3 setup.py build
3、在目录下，使用python3 setup.py sdist
4、然后会生成一个.tar.gz文件
5、下载压缩文件，解压都目录
6、进入目录，sudo python3 setup.py install 会安装包
7、卸载，需要手动找到安装包的安装目录，删除包和包相关的，两个文件夹就可以了
"""

from distutils.core import setup

setup(name ="qmg_animal",
    version="1.0", #版本号要字符哦，setup.py build 不会报错，安装会报错
    description="趣蘑菇的动物包",
    long_description="趣蘑菇的动物包，有狗类，猫类",
    author="海风",
    author_email="qumogu@qq.com",
    url="www.qumogu.com",
    py_modules=["qmg_animal.ani_dog", "qmg_animal.ani_cat"])