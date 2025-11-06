from game import Game



class Orc:

    def __init__(self, name, hp, type1, speed, power, armor_rating, weapon):
        self.name = name
        self.hp = hp
        self.type = type1
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.weapon = weapon


    def speak(self):
        return f"the {self.type} {self.name} is angeyyyy!!!"

    def attack(self,player):
        dice20 = Game.roll_dice(20)
        dice20 += self.speed
        if dice20 > player.armor_rating:
            dice6 = Game.roll_dice(6)
            dice6 += self.power
            self.update_orc()
            player.hp -= dice6
        else:print("You missed the mark.")


    def update_orc(self):
        if self.weapon == "knife":
            self.power *= 0.5
        if self.weapon == "axe":
            self.power *= 1.5

    def orc_status(self):
        return f"orc status:\nname: {self.name}\nhp: {self.hp}\ntype: {self.type}\nspeed: {self.speed}\narmor raying: {self.armor_rating}\nweapon: {self.weapon}"
