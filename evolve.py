import random


class Creature:

    def __init__(self, name):
        self.name = name
        self.teeth = 0
        self.armor = 0
        self.poison = 0
        self.resist = 0
        self.spikes = 0
        self.wins = 0
        self.games = 0

    def attack(self, other):
        if random.randint(0, 2) == 1:
            print(self.name + " attacked with teeth\n")
            other.defend(self, "teeth")
        else:
            print(self.name + " attacked with spikes\n")
            other.defend(self, "spikes")

    def defend(self, other, typey):
        attack = 0
        if typey == "teeth":
            attack = other.teeth
        elif typey == "spikes":
            attack = other.spikes

        if self.armor > attack:
            print(self.name + " defended against " + other.name)
            print(other.name + " evolved " + typey + "\n")
            if typey == "teeth":
                other.teeth += 1
            elif typey == "spikes":
                other.spikes += 1
            self.attack(other)
        else:
            print(self.name + " failed to defend against " + other.name)
            self.armor += 1
            print(self.name + " evolved armor\n")
            other.poisoning(self)

    def poisoning(self, other):
        if self.resist < other.poison:
            print(self.name + " was poisoned")
            self.resist += 1
            print(self.name + " evolved resistance\n")
            print("TIE\n")
        else:
            print(self.name + " resisted " + other.name + "'s poisoning")
            other.poison += 1
            print(other.name + " evolved poisoning\n")
            self.wins += 1
            print(self.name + " WINS\n")
        self.games += 1
        other.games += 1

    def display(self):
        print(f"{self.name}\nTeeth:{self.teeth}\nSpikes:{self.spikes}\nArmor:{self.armor}\nPoison:{self.poison}\nResistance:{self.resist}")
        print(f"Wins:{self.wins}\nGames:{self.games}\n")


Triceritops = Creature("Triceritops")
velociraptor = Creature("Velociraptor")

n = 1000
while n != 0:
    velociraptor.attack(Triceritops)
    print("New iteration\n------------------------------")
    n -= 1

velociraptor.display()
Triceritops.display()
