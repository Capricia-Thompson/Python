class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet_name):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pet_name)

    def display(self):
        print(
            f"First name: {self.first_name}\nLast name: {self.last_name}\nTreats: {self.treats}\nPet food: {self.pet_food}\nPets:")
        self.pet.display()
        return self

    def walk(self):
        self.pet.play()
        print(f"You played with {self.pet.name}!")
        return self

    def feed(self):
        self.pet.eat()
        print(f"You fed {self.pet.name}!")
        return self

    def bathe(self):
        self.pet.noise()
        print(f"{self.pet.name} got a bath!")
        return self


class Pet:
    def __init__(self, pet, energy=0, health=0):
        self.name = pet['name']
        self.type = pet['type']
        self.tricks = pet['tricks']
        self.energy = energy
        self.health = health
        self.sound = pet['sound']

    def display(self):
        print(f"Name: {self.name}\nType: {self.type}\nTricks: {self.tricks}")
        return self

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.sound * 3)
        return self


Lucky = {'name': "Lucky", 'type': "bird",
         'tricks': ["echo", "sing"], 'sound': "tweet"}
ninja1 = Ninja("Jane", "Doe", ["biscuits", "cheese", "fruit"],
               ["kibble", "grain"], Lucky)


ninja1.display().feed().walk().bathe()
