import math
import random


class Fighter:
    def __init__(self, name, hp, attack, level):
        self.name = name
        self.totalHp = hp
        self.hp = hp
        self.attack = attack
        self.xp = 0
        self.level = level
        self.level_up()
        self.wins = 0

    def heal(self, heal):
        if heal == -1:
            self.hp = self.totalHp
            print(f"{self.name} is all healed up! \n")
        else:
            self.hp += heal
            print(f"{self.name} was healed by {heal} hp.")

    def attacking(self, other):
        print(f"{self.name} attacked!")
        other.hp -= self.attack
        print(f"{other.name} took {self.attack} damage!")

        if other.hp <= 0:  # if opponent dead, faint them
            other.faint()
            print("\n" + self.name + " WINS! \n")
            self.wins += 1
            self.gain_xp(other)
            other.fail_xp(self)
        else:
            print(f"{other.name} current hp: {other.hp}\n")

    def faint(self):
        self.hp = 0
        print(f"{self.name} fainted!")

    def gain_xp(self, other):
        if self.level < 100:
            self.xp += int(math.sqrt(other.totalHp + other.attack))
            print(f"{self.name} earned {int(math.sqrt(other.totalHp + other.attack))} xp!")
            self.level_up()

    def fail_xp(self, other):
        if self.level < 100:
            self.xp += int(math.sqrt(other.totalHp + other.attack) / 2)
            print(f"{self.name} earned {int(math.sqrt(other.totalHp + other.attack) / 2)} xp for trying.")
            self.level_up()
            print()

    def level_up(self):
        while 0 <= self.xp - (self.level**2):
            if self.level < 100:
                self.xp = self.xp - (self.level**2)
                self.level += 1
                print(f"LEVEL UP! {self.name} is now level {self.level}, and at {self.xp} xp")
                self.attack += int(math.sqrt(int(math.sqrt(self.attack))))
                self.totalHp += int(math.sqrt(self.totalHp))
            else:
                break

    def display(self):
        print(f"{self.name}: {self.wins} wins, {self.totalHp} total hp, {self.hp} current hp, {self.attack} attack, lvl {self.level}, {self.xp} xp")


def fight(first, second):
    print(f"Battle between {first.name} and {second.name}, start!")
    if first.hp+first.attack > second.hp+second.attack:  # lets the weaker one go first
        temp = first
        first = second
        second = temp
    print(f"{first.name} goes first!\n")

    while (first.hp != 0) and (second.hp != 0):
        if first.hp != 0:  # first attacks
            first.attacking(second)
        if second.hp != 0:  # second attacks
            second.attacking(first)
    second.display()
    first.display()
    print()


n = 50

bene = Fighter("Bene", 25, 5, 1)
mal = Fighter("Mal", 16, 10, 1)
test = Fighter("Test", int((bene.hp+mal.hp)/2), int((bene.attack+mal.attack)/2)-1, 1)

while n > 0:
    x = random.randint(0, 3)
    if x == 0:
        fight(bene, mal)

        bene.heal(-1)
        mal.heal(-1)
    elif x == 1:
        fight(mal, test)

        mal.heal(-1)
        test.heal(-1)
    else:
        fight(bene, test)

        bene.heal(-1)
        test.heal(-1)
    n -= 1

bene.display()
mal.display()
test.display()
