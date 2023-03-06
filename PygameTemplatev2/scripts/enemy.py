from scripts.settings import *
from scripts.player import *





class Enemy(Player):
    width = 50
    height = 50
    def __init__(self, game, x, y, color,color_key):
        super(Enemy, self).__init__(game, x, y, color,color_key)
        self.xMove = -5
        self.yMove = 3


    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.enemy_group.add(self)

    def update(self):


        self.game.check_Events()
        #temporary auto move
        self.rect.x += self.xMove
        self.rect.y += self.yMove
        # #x bounce
        # if self.rect.right >= WIDTH:
        #     self.xMove = -5
        # if self.rect.left <= 0:
        #     self.xMove = 5
        # #y bounce
        # if self.rect.bottom >= HEIGHT:
        #     self.yMove = -3
        # if self.rect.top <= 0:
        #     self.yMove = 3
        # loops the screen so player goes around

        #makes stuff bouncy
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.xMove *= -1
            self.image = pg.transform.flip(self.image, True, False)
        if self.rect.top <= 0 or self.rect.bottom >= WIDTH:
            self.yMove *= -1



