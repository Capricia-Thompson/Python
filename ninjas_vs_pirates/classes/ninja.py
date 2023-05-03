import random
r1 = random.randint(11, 15)


class Ninja:

    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 10000

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, target):
        dmg = round(((self.strength/2)*r1))
        target.dodge(self, dmg)
        return self

    def dodge(self, attacker, dmg):
        if (self.speed > attacker.speed):
            print(f"{attacker.name}'s attack was too slow. You dodged!")
            return self
        elif (self.speed == attacker.speed):
            self.health -= dmg
            print(
                f"You dodged, but {attacker.name}'s attack still grazed you.\nYou lost {dmg} health points!")
            return self
        else:
            self.health -= dmg * 2
            print(
                f"{attacker.name}'s attack landed squarely. {dmg *2} health points lost!")
            return self

    def meditation(self):
        print(f"{self.name} focuses! His speed increases!")
        self.speed = self.speed*(r1/10)
        print(f"His speed is now {self.speed}")
        return self


class Jonin(Ninja):
    def __init__(self, name):
        super().__init__(name)
        self.speed += 50

    def attack(self, target):
        print(f"{self.name} used stealth attack!")


class Ninjaturtle(Ninja):
    def __init__(self, name):
        super().__init__(name)
        self.strength += 50

    def attack(self, target):
        print(
            f"Nun-CHUCK!\n{self.name} threw their nun-chucks at {target.name}!")
        super().attack(target)
