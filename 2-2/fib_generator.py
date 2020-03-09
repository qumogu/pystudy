import time


def fib(num):
    cur_num = 0
    a, b = 0, 1
    while cur_num < num:
        yield a
        a, b = b, a+b
        cur_num += 1
    return "生成器结束。"


def main():
    
    f = fib(5)

    while True:
        try:
            print(next(f))
            time.sleep(1)
        except StopIteration as e:

            print("遍历生产器完成,", e.value)
            break

if __name__ == "__main__":
    main()
