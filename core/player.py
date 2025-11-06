from game import Game


class Player:

    def __init__(self,name,hp,speed,power,armor_rating,profession):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.profession = profession


    def speak(self):
        return f"{self.name} is ready for battle"

    def attack(self,monster):
        power = Game.roll_dice(20)
        power += self.speed
        if power > monster.armor_rating:
            dice6 = Game.roll_dice(6)
            dice6 += self.power
            monster.hp -= dice6
        else: print("You missed the mark.")

    def update_player(self):
        if self.profession == "warrior":
            self.power += 2
        else: self.hp += 10

    def status_player(self):
        return f"status player:\nname: {self.name}\nhp: {self.hp}\nspeed: {self.speed}\npower: {self.power}\narmor rating: {self.armor_rating}\nprofession: {self.profession}"
