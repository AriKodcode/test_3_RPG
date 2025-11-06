import random
from core.player import Player
from core.gobin import Goblin
from core.orc import Orc
from game import Game

if __name__ == "__main__":
    player = Player("ari",50,random.randrange(5,11),random.randrange(5,11),random.randrange(5,16),random.choice(["warrior","healer"]))
    player.update_player()
    orc = Orc("gimbly",50,"orc",random.randrange(0,6),random.randrange(10, 16),random.randrange(2, 9),random.choice(["knife","sword","axe"]))
    goblin = Goblin("saromen", 20, "goblin", random.randrange(5, 11),random.randrange(5, 11),1,random.choice(["knife","sword","axe"]))
    game = Game
    game.start(game.show_menu())
    monster = game.choose_random_monster()
    player_dice = Game.roll_dice(6)
    player_dice += player.speed
    monster_dice = Game.roll_dice(6)
    monster_dice += monster.speed
    while True:
        game.battle(player, monster,player_dice,monster_dice)
        print(player.status_player())





    print(player.status_player())
    print(goblin.goblin_status())
    print(orc.orc_status())










