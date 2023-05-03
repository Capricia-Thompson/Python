import random
from classes.ninja import Ninjaturtle
from classes.pirate import Viking

michelangelo = Ninjaturtle("Michelanglo")

jack_sparrow = Viking("Jack Sparrow")

print(f"Showdown: {michelangelo.name} VS {jack_sparrow.name}!!")

while michelangelo.health > 0 and jack_sparrow.health > 0:
    player_input = ""
    while not player_input == "1" and not player_input == "2":
        player_input = input(
            "Decide!\n 1) Attack!\n 2) Meditate!\n <===========>")
        if player_input == "1":
            michelangelo.attack(jack_sparrow)
        elif player_input == "2":
            michelangelo.meditation()
        else:
            print("This isn't a game, fool! Decide!")

    coin_toss = random.randint(1, 2)
    if coin_toss == 1:
        jack_sparrow.attack(michelangelo)
    else:
        jack_sparrow.ramp_up()

    if michelangelo.health > 0 and jack_sparrow.health <= 0:
        print("You're victorious!")
    elif michelangelo.health <= 0 and jack_sparrow.health <= 0:
        print("Massacre!")
    elif michelangelo.health <= 0 and jack_sparrow.health > 0:
        print(f"{jack_sparrow.name} steals the kill!")
