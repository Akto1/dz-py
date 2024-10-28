import time
import random

class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 50  
        self.energy = 50  
        self.happiness = 50  

    def eat(self):
        if self.hunger > 10:
            print(f"{self.name} поел и чувствует себя сытым!")
            self.hunger -= 10
            self.energy += 5
        else:
            print(f"{self.name} не хочет есть.")
        self.status()

    def play(self):
        if self.energy > 10:
            print(f"{self.name} играет и веселится!")
            self.hunger += 10
            self.energy -= 15
            self.happiness += 10
        else:
            print(f"{self.name} слишком устал, чтобы играть.")
        self.status()

    def sleep(self):
        print(f"{self.name} спит и набирается сил.")
        time.sleep(1)  
        self.energy = min(self.energy + 30, 100)
        self.happiness += 5
        self.hunger += 5
        self.status()

    def status(self):
        print(f"\nСостояние {self.name}:")
        print(f"Голод: {self.hunger}/100")
        print(f"Энергия: {self.energy}/100")
        print(f"Счастье: {self.happiness}/100\n")

    def live(self):
        actions = [self.eat, self.play, self.sleep]
        while True:
            action = random.choice(actions)
            action()
            if self.hunger >= 100:
                print(f"{self.name} очень голоден и уходит на поиски еды.")
                break
            elif self.happiness <= 0:
                print(f"{self.name} грустит и уходит искать радость в другом месте.")
                break
            elif self.energy <= 0:
                print(f"{self.name} вымотан и нуждается в отдыхе.")
                break
            time.sleep(2)  
my_pet =  Pet("Барсик","котик")
my_pet.live()