import pygame as pg
import random

running = pg.image.load('images/playerrun1.png')
running2 = pg.image.load('images/playerrun2.png')
running3 = pg.image.load('images/playerrun3.png')
running4 = pg.image.load('images/playerrun4.png')
running5 = pg.image.load('images/playerrun5.png')
running6 = pg.image.load('images/playerrun6.png')
running7 = pg.image.load('images/playerrun7.png')
running8 = pg.image.load('images/playerrun8.png')
player_image = pg.image.load("images/player.png")
player1=pg.image.load("images/player1.png")
enemy_image = pg.image.load("images/enemy.png")
ranged_image = pg.image.load("images/ranged.png")
background = pg.image.load("images/bg.png")

background = pg.transform.scale(background,(1024,560))
running = pg.transform.scale(running,(35,35))
running2 = pg.transform.scale(running2,(35,35))
running3 = pg.transform.scale(running3,(35,35))
running4 = pg.transform.scale(running4,(35,35))
running5 = pg.transform.scale(running5,(35,35))
running6 = pg.transform.scale(running6,(35,35))
running7 = pg.transform.scale(running7,(35,35))
running8 = pg.transform.scale(running8,(35,35))
player1=pg.transform.scale(player1,(35,35))
player_imageimage = pg.transform.scale(player_image,(35,35))
ranged_imageimage = pg.transform.scale(ranged_image,(30,30))

class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites,enemies): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0
        self.standing = True
        self.running = False
        self.image = player_imageimage
        self.rect = self.image.get_rect()
        self.standing_frames =[player1,player_imageimage]
        self.running_frames = [running,running2,running3,running4,running5,running6,running7,running8]
        self.pos_x = 50
        self.pos_y = 400
        self.speed = 3
        self.hp = 100
        self.all_sprites = all_sprites
        self.enemies = enemies
        self.cooldown = 0
        self.maxcooldown = 20
        


    def take_dmg(self, dmg):
        self.hp -= dmg 
        if self.hp <= 0:
            pg.quit()

    def attack(self):
        if self.cooldown <= 0:
            projectile = ranged_attack(self.pos_x, self.pos_y,self.enemies)
            print("attacked")
            projectile.add(self.all_sprites)
            self.cooldown = 25
        

    def update(self):
        self.animate()
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.standing = True
        self.cooldown -= 1
        
        if self.pos_y > 560:
            self.pos_y = 560
        if self.pos_y < 200:
            self.pos_y = 200
        
        
       

        # player input
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # oppover
            self.pos_y -= self.speed
            self.standing=False
            self.running=True
        if keys[pg.K_s]: # nedover
            self.pos_y += self.speed
            self.standing=False
            self.running=True
        if keys[pg.K_a]: # venstre
            self.pos_x -= self.speed
            self.standing=False
            self.running=True
        if keys[pg.K_d]: # høyre
            self.pos_x += self.speed 
            self.standing=False
            self.running=True
        if keys[pg.K_f]:
            self.attack()
    def animate(self):
        now = pg.time.get_ticks()
        if self.standing:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame =(self.current_frame +1)%len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect=self.image.get_rect()
        if self.running:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame +1)%len(self.running_frames)
                self.image = self.running_frames[self.current_frame]
                self.rect=self.image.get_rect()

class Enemy(pg.sprite.Sprite):
    def __init__(self, player): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 1200
        self.pos_y = random.randint(200,560)
        self.speed = random.randint(3,5)
        self.player = player

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.pos_x -= self.speed
        if self.pos_x < -10:
            self.kill()
        

        if self.pos_y > self.player.pos_y:
            self.pos_y -= 1
        if self.pos_y < self.player.pos_y:
            self.pos_y += 1
class ranged_attack(pg.sprite.Sprite):
    def __init__(self,x,y,enemies):
        pg.sprite.Sprite.__init__(self)
        self.image = ranged_imageimage
        self.rect = self.image.get_rect()

        self.pos_x = x
        self.pos_y = y
        self.speed = 2
        self.enemies = enemies

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.pos_x += self.speed
        hits = pg.sprite.spritecollide(self,self.enemies, True)


