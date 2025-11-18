class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Objects
a = Animal()
d = Dog()
c = Cat()

for obj in (a, d, c):
    obj.speak()   # same method name, different output
