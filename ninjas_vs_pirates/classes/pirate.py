import random
r1 = random.randint(1, 5)
r2 = random.randint(11, 15)


class Pirate:

    def __init__(self, name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 10000

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, target):
        dmg = ((self.strength/2)*r1)
        target.dodge(self, dmg)
        return self

    def dodge(self, attacker, dmg):
        if (self.speed > attacker.speed):
            print(f"{attacker.name}'s attack was too slow. You dodged!")
            return self
        elif (self.speed == attacker.speed):
            self.health -= dmg
            print(
                f"You dodged, but {attacker.name}'s attack still grazed you.\nYou lost {dmg} health!")
            return self
        else:
            self.health -= dmg * 2
            print(
                f"{attacker.name}'s attack landed squarely. {dmg *2} health lost!")
            return self

    def ramp_up(self):
        print(
            f"AAARRRRGGG!! {self.name} uses battle cry to increase his strength!")
        self.strength = self.strength*(r2/10)
        print(f"His strength is now {self.strength}")
        return self


class Viking(Pirate):
    def __init__(self, name):
        super().__init__(name)
        self.strength += 50

    def attack(self, target):
        print(f"{self.name} swings his battle axe!")
        super().attack(target)


class Buccaneer(Pirate):
    def __init__(self, name):
        super().__init__(name)
        self.speed += 10

    def attack(self, target):
        print(f"{self.name} slashes with his hook!")
