# OOP - inheritance and polymorphism

class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
            quack = "Quack!",
            feathers = "The duck has grey and white feathers.",
            bark = "This duck cannot bark.",
            fur = "This duck has no fur."
            )
class Person(AnimalActions):
    strings = dict(
            quack = "This person quacks like a duck!",
            feathers = "This person takes a feather from the ground.",
            bark = "This person says woof!",
            fur = "This person has a lot of head hair."
            )

class Dog(AnimalActions):
    strings = dict(
            quack = "The dog cannot quack.",
            feathers = "This dog has no feathers.",
            bark = "The dog lets out a loud bark!",
            fur = "This is the furriest dog ever."
            )

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donald = Duck()
    david = Person()
    lucy = Dog()

    print("- In the forest:")
    for o in (donald, david, lucy):
        in_the_forest(o)

    print("- In the doghouse:")
    for i in (donald, david, lucy):
        in_the_doghouse(i)

if __name__ == "__main__": main()
