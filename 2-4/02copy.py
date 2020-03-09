
import copy
import time


def main():
    list_a = [11, 22]
    list_b = [33, 44]
    list_c = [list_a, list_b]

    list_d = list_c

    list_e = copy.copy(list_c)
    
    list_f = copy.deepcopy(list_c)

    print("变量a，值：%s,引用地址：%d" % (list_a, id(list_a)))
    print("变量b，值：%s,引用地址：%d" % (list_b, id(list_b)))
    print("变量c，值：%s,引用地址：%d" % (list_c, id(list_c)))
    print("变量d，值：%s,引用地址：%d" % (list_d, id(list_d)))
    print("变量e，值：%s,引用地址：%d" % (list_e, id(list_e)))
    print("变量f，值：%s,引用地址：%d" % (list_f, id(list_f)))
    list_a.append(55)
    # input("按回车继续") 
    time.sleep(3)
    print("")

    print("变量a追加一个55看大家的数据变化")
    input("按回车看结果i：") 
    print("")
    print("变量c，值：%s" % list_c)
    print("变量d，值：%s" % list_d)
    print("变量e，值：%s" % list_e)
    print("变量f，值：%s" % list_f)
    
    # time.sleep(3)
    list_c.append(66)
    print("变量c[0]追加一个55看大家的数据变化")
    input("按回车看结果i：") 
    print("")
    print("变量c，值：%s" % list_c)
    print("变量d，值：%s" % list_d)
    print("变量e，值：%s" % list_e)
    print("变量f，值：%s" % list_f)
    
    # time.sleep(3)
    print("下面，看，a,c[0],d[0],e[0],f[0]的引用地址")
    input("按回车看结果：")
    print("")
    print("a的内存地址:%d" %  id(list_a))
    print("c[0]的内存地址:%d" %  id(list_c[0]))
    print("d[0]的内存地址:%d" %  id(list_d[0]))
    print("e[0]的内存地址:%d" %  id(list_e[0]))
    print("f[0]的内存地址:%d" %  id(list_f[0]))


if __name__ == '__main__':
    main()
