

class Dog(object):
    
    def __init__(self,name):
        
        self.name = name


    def play_game(self):
        
        print("%s蹦蹦跳跳的玩撒……" % self.name)


class FlyDog(Dog):

    def play_game(self):
        
        print("%s上天入地的玩撒……" % self.name)
    

    def run(self):
        pass

class Person(object):

    def __init__(self, name):
        
        self.name = name

    def play_with_dog(self, dog):
        
        print("%s愉快的与爱犬%s在一起玩……" % (self.name, dog.name))
        dog.play_game()
    

    def fly(self):
        pass

class Test(object):
    pass

class XiaoDog(Dog, Test):
    pass


def main():
    
    dog = Dog("旺财")
    print(dir(dog))

    p = Person("小明")
    p.play_with_dog(dog)

    f_dog = FlyDog("哮天犬")
    
    p.play_with_dog(f_dog)

    x_dog = XiaoDog("Spuer")
    x_dog.play_game()
    print(XiaoDog.__mro__)


if __name__ == "__main__":
    main()
