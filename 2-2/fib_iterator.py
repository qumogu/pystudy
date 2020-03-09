from collections import Iterable
from collections import Iterator
import time


class FibFuc():
    
    def __init__(self,num):
        
        self.a = 0
        self.b = 1
        self.current_num = 0
        self.num = num


    def __iter__(self):

        return self

    def __next__(self):
        
        if self.current_num < self.num:
            tmp = self.a
            #print(self.a)
            #yield self.a
            self.a,self.b = self.b,self.a + self.b
            self.current_num += 1
            return tmp
        else:
            raise StopIteration
        


def main():
    
    fib = FibFuc(10)
    for f in fib:
        print(f)
        time.sleep(1)
    
    list_fib = list(FibFuc(8))
    print(list_fib)

    fib = FibFuc(10)
    print(tuple(fib))


if __name__ == "__main__":
    main()
