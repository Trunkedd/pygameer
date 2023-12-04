import pygame as pg
import math
from sprites import *
import random
pg.init() # starter pygame modul

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)  
YELLOW = (255,255,0)

screen = pg.display.set_mode((1024,560)) # lager spill vindu, 800x600
WIDTH = 1024


clock = pg.time.Clock()
font_times40 = pg.font.SysFont("Times New Roman",20)

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()


player = Player(all_sprites,enemies)
all_sprites.add(player)

i = 0
playing = True
while playing: # game loop
    clock.tick(120)
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            playing = False
            pg.quit()
  
    # spawning av flere players
    if len(enemies) < 10:
        new_enemy = Enemy(player)
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

    # oppdater alle sprites i all_sprites gruppen
    all_sprites.update()
     
     # collision
    hits = pg.sprite.spritecollide(player, enemies,True)
    if hits:
        player.take_dmg(10)
        print(player.hp)

    hp_text = font_times40.render(f"HP: {player.hp}", False ,(GREEN))
    # tegn bakgrunn og alle sprites
    screen.blit(background,(i,0))
    screen.blit(background,(WIDTH+i,0))
    if (i == -WIDTH):
        screen.blit(background,(WIDTH+i,0))
        i=0
    i-=1
    all_sprites.draw(screen)
    screen.blit(hp_text,(10,10))
    pg.display.update()