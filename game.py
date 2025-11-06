from core.player import Player
from core.orc import Orc
from core.gobin import Goblin
import random


class Game:

    @staticmethod
    def start(show_menu):
        print("GAME START!")
        return show_menu

    @staticmethod
    def show_menu():
        while True:
            choose = input("if you wont start game press B, if you wont exit press E")
            if choose == "B":
                return True
            elif choose == "E":
                return False
            else:
                print("Error press only B or E")

    @staticmethod
    def choose_random_monster():
        choose = random.choice(["ork", "goblin"])
        return choose

    @staticmethod
    def battle(player: Player, monster, p_dice, m_dice):
        if p_dice > m_dice:
            print("player its your turn")
            Player.attack(player,monster)

        else:
            print("monster its your turn")
            monster.attack(player)

    @staticmethod
    def roll_dice(dice_number):
        if dice_number == 6:
            return random.randrange(1, 7)
        else:
            return random.randrange(1, 21)
