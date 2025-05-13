
class Superhero:
    def __init__(self, name, power, city):
        self.name = name  # Name of our superhero, think Superman, Spiderman, etc.!
        self.power = power  # The superhero's power, like super strength or flying.
        self.city = city  # The city they protect. Keepin' it simple for now.

    def introduce(self):
        # A basic intro to let the superhero tell us a bit about themselves!
        print(f"Hi, I'm {self.name}! I protect {self.city} using my {self.power}.")

# Let's make a more advanced superhero by adding some special abilities to our Speedster!

class Speedster(Superhero):
    def __init__(self, name, power, city, speed):
        super().__init__(name, power, city)  # Inheriting from Superhero class
        self.speed = speed  # This is the superhero’s speed, the faster the better! 🏃‍♂️

    def introduce(self):
        # Overriding the intro to include the superhero’s speed. Because... why not?
        super().introduce()  # Calling the original intro from Superhero class
        print(f"My top speed is {self.speed} mph! Yes, I'm THAT fast!")

# Now let's test it out! Create a Speedster and see how they introduce themselves:
flash = Speedster("Flash", "Super Speed", "Central City", 1000)
flash.introduce()  # The Flash should introduce himself and tell us how fast he is! 🚀

