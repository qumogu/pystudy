

import copy

def main():
	
	a = "hello,world"

	b = {"tuple":(11,55),
		 "name":"jack",
		"age":18}

	c = a
	d = b

	e = copy.copy(a)
	f = copy.copy(b)

	h = copy.deepcopy(a)
	i = copy.deepcopy(b)
 
		
	print("a的值：%s，内存地址：%d" % (a, id(a)))
	print("b的值：%s，内存地址：%d" % (b, id(b)))
	print("c是a的引用，c的值：%s，内存地址：%d" % (c, id(c)))
	print("d是b的引用，d值：%s，内存地址：%d" % (d, id(d)))
	print("e是a的浅拷贝，e的值：%s，内存地址：%d" % (e, id(e)))
	print("f是b的浅拷贝，f的值：%s，内存地址：%d" % (f, id(f)))
	print("h是a的深拷贝，h的值：%s，内存地址：%d" % (h, id(h)))
	print("i是b的深拷贝，i的值：%s，内存地址：%d" % (i, id(i)))



if __name__ == "__main__":
	main()
