import pygame
from pygame import mixer
from pyglet import image
import os
import math
import time
import random
pygame.init()
screen=pygame.display.set_mode((700,700))

title=pygame.display.set_caption("My first game")
icon_image=pygame.image.load("/Users/vishalvenkat/Desktop/pygame/second/images/lotr.jpg")
icon=pygame.display.set_icon(icon_image)

running=True
wizard=pygame.image.load("/Users/vishalvenkat/Desktop/pygame/second/images/wizard.png")
wizard_x=120
wizard_y=560
wizard_change_x=0
wizard_change_y=0

fireball=pygame.image.load("/Users/vishalvenkat/Desktop/pygame/second/images/fireball.png")
fireball_x=0
fireball_y=560
fireball_change_x=9.5
fireball_change_y=0
fireball_state="ready"
smaug_short_dialogues = [
    "I am fire!",
    "You dare disturb me?",
    "Run, little one!",
    "Feel my wrath!",
    "Bow before me!",
    "No escape, thief!"
]
gandalf_speeches = [
    "You shall not pass!",
    "A wizard is never late.",
    "Fly, you fools!",
    "You have no power here.",
    "One ring to rule them all.",
    "I am a servant of the Secret Fire."
]

smaugfont=pygame.font.Font("freesansbold.ttf",22)
bg=pygame.image.load("/Users/vishalvenkat/Desktop/pygame/second/images/background.jpeg")
res_bg = pygame.transform.scale(bg, (700, 700))

planet=pygame.image.load("/Users/vishalvenkat/Desktop/pygame/second/images/jupiter.png")
ground=pygame.image.load("/Users/vishalvenkat/Desktop/pygame/second/images/ground.png")

number=0
def dialogues():
    if game_state == "playing":
        text = smaugfont.render(smaug_short_dialogues[number], True, 'black')
        gtext=smaugfont.render(gandalf_speeches[number], True, 'black')
        screen.blit(text, (dragon_x - 16, dragon_y - 16))
        screen.blit(gtext, (wizard_x - 16, wizard_y - 16))



    
dragon=pygame.image.load("/Users/vishalvenkat/Desktop/pygame/second/images/dragon.png")

dragon_x=random.randint(620,680)
dragon_y=560
dragon_y_change=0
dragon_x_change=-1.1

font=pygame.font.Font("freesansbold.ttf",32)
score_value=0
def show_score():
    score=font.render("Score : "+ str(score_value),True,(0,255,0))
    screen.blit(score,(10,10))

finished=pygame.font.Font("freesansbold.ttf",42)
finish=finished.render("GAME OVER!",True,'black')

game_state = "playing"
game_over=False
update_dialogue = False 

def fire(x):
    global fireball_state
    fireball_state="fire"
  
    
    screen.blit(fireball,(x+16,fireball_y+10))

def show_wizard():
    screen.blit(wizard,(wizard_x,wizard_y))

def show_dragon():
    screen.blit(dragon,(dragon_x,dragon_y))

def iscollision():
    distance=math.sqrt(math.pow(dragon_y-fireball_y,2)+math.pow(dragon_x-fireball_x,2))
    if distance<22:
        return True
    else:
        return False
def game_over_text():
    over_text = finished.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text, (200, 50))    
  
while running:
    screen.fill((0,0,0))
    screen.blit(res_bg,(0,0))
    screen.blit(planet,(600,60))
    screen.blit(ground,(0,625))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                wizard_change_x=-5.3
            if event.key==pygame.K_RIGHT:
                wizard_change_x=5.3
            if event.key == pygame.K_SPACE:
               
                fireball_x = wizard_x
                fire(fireball_x)  
                    
        if event.type==pygame.KEYUP:
            wizard_change_x=0             
    

  

    wizard_x+=wizard_change_x
    dragon_x+=dragon_x_change
    if wizard_x<=0:
        wizard_x=0
    elif wizard_x>=636:
        wizard_x=636
    if  fireball_state is "fire":
        fire(fireball_x) 
        fireball_x+=fireball_change_x
    if fireball_x>900:
        fireball_x=150 
        fireball_state="ready"
        fireball_y-=fireball_change_y 
    collision=iscollision()
    if collision:
        fireball_state="ready"
        fireball_x=150 
        dragon_x=random.randint(620,680)
        dragon_y=560 
        score_value+=1
        number+=1
        if number>5:
            number=0

       
          

          
    if dragon_x<=180:
        print("Dragon reached 180!")
        dragon_x=100000000
        game_state = "game over"
        game_over = True
       
        
    show_wizard()
    show_dragon()
    show_score()
    dialogues()
    if game_state == "game over":
       game_over_text()
       pygame.display.update()
       time.sleep(1)
       
       break
           
    pygame.display.update()        
