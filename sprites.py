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
player_image = pg.image.load("images/idle.png")
player1 = pg.image.load("images/idle1.png")
player2 = pg.image.load("images/idle2.png")
player3 = pg.image.load("images/idle3.png")
player4 = pg.image.load("images/idle4.png")
player5 = pg.image.load("images/idle5.png")
player6 = pg.image.load("images/idle6.png")
player7 = pg.image.load("images/idle7.png")
attack1 = pg.image.load("images/attack1.png")
attack2 = pg.image.load("images/attack2.png")
attack3 = pg.image.load("images/attack3.png")
attack4 = pg.image.load("images/attack4.png")
attack5 = pg.image.load("images/attack5.png")
enemy_image = pg.image.load("images/enemy.png")
enemy_image1 = pg.image.load("images/enemy1.png")
enemy_image2 = pg.image.load("images/enemy2.png")
enemy_image3 = pg.image.load("images/enemy3.png")
enemy_image4 = pg.image.load("images/enemy4.png")
enemy_image5 = pg.image.load("images/enemy5.png")
ranged_image = pg.image.load("images/ranged.png")
background = pg.image.load("images/bg.png")

background = pg.transform.scale(background,(1024,560))
running = pg.transform.scale(running,(50,50))
running2 = pg.transform.scale(running2,(50,50))
running3 = pg.transform.scale(running3,(50,50))
running4 = pg.transform.scale(running4,(50,50))
running5 = pg.transform.scale(running5,(50,50))
running6 = pg.transform.scale(running6,(50,50))
running7 = pg.transform.scale(running7,(50,50))
running8 = pg.transform.scale(running8,(50,50))
attack1 = pg.transform.scale(attack1,(50,50))
attack2 = pg.transform.scale(attack2,(50,50))
attack3 = pg.transform.scale(attack3,(50,50))
attack4 = pg.transform.scale(attack4,(50,50))
attack5 = pg.transform.scale(attack5,(50,50))
player1=pg.transform.scale(player1,(50,50))
player2=pg.transform.scale(player2,(50,50))
player3=pg.transform.scale(player3,(50,50))
player4=pg.transform.scale(player4,(50,50))
player5=pg.transform.scale(player5,(50,50))
player6=pg.transform.scale(player6,(50,50))
player7=pg.transform.scale(player7,(50,50))
attack1=pg.transform.scale(player1,(50,50))
player_imageimage = pg.transform.scale(player_image,(50,50))
ranged_imageimage = pg.transform.scale(ranged_image,(30,30))

class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites,enemies): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0
        self.standing = True
        self.running = False
        self.is_melee = False
        self.image = player_imageimage
        self.rect = self.image.get_rect()
        self.attack_cooldown = 0
        self.standing_frames =[player1,player_imageimage]
        self.running_frames = [running,running2,running3,running4,running5,running6,running7,running8]
        self.attack_frames = [attack1,attack2,attack3,attack4,attack5]
        self.pos_x = 50
        self.pos_y = 400
        self.speed = 3
        self.hp = 100
        self.all_sprites = all_sprites
        self.enemies = enemies
        self.cooldown = 0
        self.maxcooldown = 20
        


    def take_dmg(self,dmg):
        self.hp -= dmg 
        if self.hp <= 0:
            pg.quit()
            print("you died")
            
    def meleeattacking(self):
        if self.attack_cooldown == 0:
            self.attack_cooldown = 1
            meleeprojectile = meleeattack(self.rect.center,self.enemies)
            meleeprojectile.add(self.all_sprites)
            self.is_melee = True
            self.standing=False
            self.running=False
            return meleeprojectile
    def attack(self):
        if self.cooldown <= 0:
            projectile = ranged_attack(self.pos_x, self.pos_y,self.enemies)
            print("attacked")
            projectile.add(self.all_sprites)
            self.cooldown = 35
        

    def update(self):
        self.animate()
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.standing = True
        self.cooldown -= 1
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
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
            self.is_melee = False
        if keys[pg.K_s]: # nedover
            self.pos_y += self.speed
            self.standing=False
            self.running=True
            self.is_melee = False
        if keys[pg.K_a]: # venstre
            self.pos_x -= self.speed
            self.standing=False
            self.running=True
            self.is_melee = False
        if keys[pg.K_d]: # høyre
            self.pos_x += self.speed 
            self.standing=False
            self.running=True
            self.is_melee = False
        if keys[pg.K_f]:
            self.attack()
        if keys[pg.K_SPACE]:
            self.meleeattacking()
            
            
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

        
        if self.is_melee:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.attack_frames)
                self.image = self.attack_frames[self.current_frame]
                self.rect=self.image.get_rect()

        
class Enemy(pg.sprite.Sprite):
    def __init__(self, player): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.enemies= True
        self.current_frame = 0
        self.last_update = 0
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.enemies_frames = [enemy_image,enemy_image1,enemy_image2,enemy_image3,enemy_image4,enemy_image5]
        self.pos_x = 1200
        self.pos_y = random.randint(0,560)
        self.speed = random.randint(3,5)
        self.player = player

    def update(self):
        self.animate()
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.pos_x -= self.speed
        self.enemies = True
        if self.pos_x < -10:
            self.kill()
        

        if self.pos_y > self.player.pos_y:
            self.pos_y -= 1
        if self.pos_y < self.player.pos_y:
            self.pos_y += 1
    def animate(self):
        now = pg.time.get_ticks()
        if self.enemies:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame +1)%len(self.enemies_frames)
                self.image = self.enemies_frames[self.current_frame]
                self.rect=self.image.get_rect()

class meleeattack(pg.sprite.Sprite):
    def __init__(self, position,enemies,):
        super().__init__()
        self.image = pg.Surface((60,30))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,255,0))
        self.rect = self.image.get_rect(center=position)
        self.lifetime = 10
        self.rect.right += 35
        self.enemies = enemies
    def update(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()
        hits =pg.sprite.spritecollide(self,self.enemies, True)


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


