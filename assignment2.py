
class Animal:
    def move(self):
        # Just a generic move method. Not very specific, but it’s a start.
        print("This animal moves in some way, not very specific though...")

# Now, let’s get more specific. Let’s make a Dog class:
class Dog(Animal):
    def move(self):
        # Dogs run! We all know that, right? 🐕
        print("The dog runs on four legs.")

# Birds fly, so let’s make a Bird class:
class Bird(Animal):
    def move(self):
        # Birds don’t walk, they fly! 🕊️
        print("The bird flies in the sky.")

# Fish... well, they swim. Let's add a Fish class:
class Fish(Animal):
    def move(self):
        # Fish move by swimming. Obviously! 🐟
        print("The fish swims in the water.")

# Let’s create some animals and see how they move. We'll use polymorphism in action here.
dog = Dog()
bird = Bird()
fish = Fish()

# Here comes the magic! Let’s make them all move, and each one will do it in their own special way:
animals = [dog, bird, fish]

for animal in animals:
    animal.move()  # Each animal calls its own move method, but they all do it differently!

