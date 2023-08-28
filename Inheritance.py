class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")

# 创建 Animal、Dog 和 Cat 的实例
animal = Animal("Animal")
dog = Dog("Dog")
cat = Cat("Cat")

# 调用各个实例的 speak 方法
animal.speak()  # 输出: Animal speaks
dog.speak()     # 输出: Woof!
cat.speak()     # 输出: Meow!