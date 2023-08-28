class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Mammal:
    def eat(self):
        print("Mammal eats")

class Dog(Animal, Mammal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")

# 创建 Dog 的实例
dog = Dog("Dog")

# 调用 Dog 实例的方法
dog.speak()  # 输出: Woof!
dog.eat()    # 输出: Mammal eats