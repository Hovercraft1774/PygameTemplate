from scripts.settings import *


class Player(pg.sprite.Sprite):#must be a sprite inherited otherwise it won't fit in groups

    def __init__(self,game,x,y,img_dir,color_key):
        super(Player,self).__init__()

        # self.player_img = pg.transform.flip(self.player_img, True, True) #this flips the image along the x,y axis
        self.image = self.get_image(img_dir)
        self.image.set_colorkey(color_key)#gets rid of black color and makes it transparent
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.game = game #adds reference to the game

        self.leftClick = False
        self.mouseMovement = False
        self.xMove = 0
        self.yMove = 0
        self.solidbounds = solidbounds
        self.bouncy = bouncy
        self.invincible = spawn_invincibility #make invincible at first because ENEMY CHEAT

        self.addToGroups()

    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.player_group.add(self)

    def get_image(self,img_dir):
        self.img = pg.image.load(img_dir).convert()
        self.img = pg.transform.scale(self.img, (TILE_SIZEX, TILE_SIZEY))
        return self.img





    def update(self):

        if self.mouseMovement == True:
            #make the character follow mouse
            self.rect.center = pg.mouse.get_pos()
            self.leftClick = pg.mouse.get_pressed()[0]




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

        if self.solidbounds:
            if self.rect.right >= WIDTH:
                self.rect.right = WIDTH
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT

            if self.rect.left <= 0:
                self.rect.left = 0

            if self.rect.top <= 0:
                self.rect.top = 0
        else:
            if self.rect.left > WIDTH:
                self.rect.right = 0
            if self.rect.top > HEIGHT:
                self.rect.bottom = 0

            if self.rect.right < 0:
                self.rect.left = WIDTH

            if self.rect.bottom < 0:
                self.rect.top = HEIGHT

        if self.bouncy:

            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.xMove *= -1
            if self.rect.top <= 0 or self.rect.bottom >= WIDTH:
                self.yMove *= -1



        if self.xMove == 0 and self.yMove == 0:
            self.image = self.get_image(player_img)
        if self.xMove > 0:
            self.image = self.get_image(player_img_move)
        if self.xMove < 0:
            self.image = self.get_image( player_img_move)
            self.image = pg.transform.flip(self.image, True, False)
        if self.bouncy == False:
            if self.yMove > 0:
                self.image = self.get_image(player_img_down)
            if self.yMove < 0:
                self.image = self.get_image(player_img_up)
