from scripts.settings import *
from scripts.player import *
from scripts.enemy import *


class Game(object):

    def __init__(self):
        self.playing = True
        pg.init()
        pg.mixer.init() #if using online editor, take this out
        # creates a screen for the game
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE) #Title of the screen window
        # creates time
        self.clock = pg.time.Clock()

        # create Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.defaultColor = DEFAULT_COLOR
        self.deathList = [] #makes list for creepy stuff
        self.kill = False
        for i in range(6):
            self.deathList.append(random.randint(0,500)) #makes list for potential creepy







        #create player player objects
        self.player = Player(self,WIDTH/4,HEIGHT/4,player_img,self.defaultColor)




        #create enemy objects
        for i in range(6):
            if 1 not in self.deathList: #if there is creepy in list
                Enemy(self,random.randint(0+Enemy.width,WIDTH-Enemy.width),
                      random.randint(0+Enemy.height,HEIGHT-Enemy.height),enemy_img,self.defaultColor)
            else:
                Enemy(self, random.randint(0 + Enemy.width, WIDTH - Enemy.width),
                      random.randint(0 + Enemy.height, HEIGHT - Enemy.height), enemyCreep_img, self.defaultColor)
                self.DEFAULT_COLOR = RED





    def gameLoop(self):
        while self.playing:
            #tick clock
            self.clock.tick(fps)

            #check events
            self.check_Events()

            #update all
            self.update()

            #draw
            self.draw()


    def check_Events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                if event.key == (pg.K_r and pg.K_g and pg.K_b):
                    self.screen_color = random.choice(colors)
                if event.key == pg.K_w:
                    self.player.yMove = 0
                if event.key == pg.K_s:
                    self.player.yMove = 0
                if event.key == pg.K_a:
                    self.player.xMove = 0
                if event.key == pg.K_d:
                    self.player.xMove = 0
                if event.key == pg.K_p or pg.K_o or pg.K_g:
                    self.player.invincible = False

            if event.type == pg.KEYDOWN:
                self.player.invincible = False #no invincibility for you
                if event.key == pg.K_p:
                    self.player.solidbounds = not (self.player.solidbounds)
                if event.key == pg.K_b:
                    self.player.bouncy = not(self.player.bouncy)
                    if self.player.bouncy:
                        self.player.xMove = 5
                        self.player.yMove = 3
                    else:
                        self.player.xMove = 0
                        self.player.yMove = 0
                if event.key == pg.K_m:
                    self.player.mouseMovement = not self.player.mouseMovement
                    self.kill = not self.kill

        # checks if a key is pressed
        keys = pg.key.get_pressed()
        if keys[pg.K_w or pg.K_UP]:  # if key is being pressed, move up
            self.player.yMove = -5
        if keys[pg.K_s or pg.K_DOWN]:  # if key is being pressed, move down
            self.player.yMove = 5
        if keys[pg.K_a or pg.K_LEFT]:  # if key is being pressed, move left
            self.player.xMove = -5
        if keys[pg.K_d or pg.K_RIGHT]:  # if key is being pressed, move right
            self.player.xMove = 5
        if keys[pg.K_p and pg.K_o and pg.K_g]:
            self.player.invincible = True

        #if single sprite hit anything in blank group, kill group object?
        # hits = pg.sprite.spritecollide(self.player,self.enemy_group,False)
        #if group hit group, kill group1 or 2
        if self.player.invincible and self.kill:
            hits = pg.sprite.spritecollide(self.player,self.enemy_group,True)
        if not self.player.invincible: #checks for invincibility
            hits = pg.sprite.groupcollide(self.player_group,self.enemy_group,True,False)
            if hits:
                print("You Died")
                self.playing = False



        if self.player.mouseMovement == True:
            pg.mouse.set_visible(False)
        else:
            pg.mouse.set_visible(True)




    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(self.defaultColor)
        self.all_sprites.draw(self.screen)



        # think whiteboard, must be last line
        pg.display.flip()

    def start_Screen(self):
        pass
    def end_Screen(self):
        pass