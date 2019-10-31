import pygame
import time
import random
import sys
pygame.init()

# Colors
white = (200, 200, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("DOOM Gurpreet")
pygame.display.update()
clock = pygame.time.Clock()
carimg=pygame.image.load('cr.JPG')
whi=pygame.image.load('4.JPG')
ylw=pygame.image.load('3.JPG')
gree=pygame.image.load('6.JPG')
bck=pygame.image.load('bck.JPG')
bck1=pygame.image.load('bck1.JPG')
car_wd=50

def intro_bck():
    intro=True
    while intro:
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        sys.exit()
         gameWindow.blit(bck,(0,0))
         largertext=pygame.font.Font("freesansbold.ttf",35)
         rav,peet=text_obj("DOOM 2529",largertext)
         peet.center=(350,115)
         gameWindow.blit(rav,peet)
         button("Start",300,520,100,50,red,white,"Play")
         button("Quit",450,520,100,50,red,white,"Quit")
         button("Intro",600,520,100,50,red,white,"Intro")
         pygame.display.update()
         clock.tick(40)
         
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    clicked=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameWindow,ac,(x,y,w,h))
        if clicked[0]==1 and action!= None:
            if action =="Play":
                gameloop()
            elif action == "Quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "Intro":
                introduction()
            elif action == "Menu":
                intro_bck()
                      
        else:
            pygame.draw.rect(gameWindow,ic,(x,y,w,h))
            stext=pygame.font.Font("freesansbold.ttf",25)
            rav,peet=text_obj(msg,stext)
            peet.center=((x+(w/2)),(y+(h/2)))
            gameWindow.blit(rav,peet)

def introduction():
    intro=True
    while intro:
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        sys.exit()
         gameWindow.blit(bck1,(0,0))
         largertext=pygame.font.Font("freesansbold.ttf",135)
         stext=pygame.font.Font("freesansbold.ttf",35)
         mtext=pygame.font.Font("freesansbold.ttf",65)
         srav,speet=text_obj("DOOM 2529  Introduction",largertext)
         speet.center=(320,100)
         frav,fpeet=text_obj("A for Speed",stext)
         fpeet.center=(400,100)
         rav,peet=text_obj("DOOM 2529  Introduction",mtext)
         peet.center=(370,100)
         gameWindow.blit(srav,speet)
         gameWindow.blit(frav,fpeet)
         gameWindow.blit(rav,peet)
         button("Back",550,520,100,50,red,white,"Menu")
         pygame.display.update()
         clock.tick(40)
                
        
def obstical(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load('car.JPG')
    elif obs==1:
        obs_pic=pygame.image.load('car1.JPG')
    elif obs==2:
        obs_pic=pygame.image.load('car2.JPG')
    elif obs==3:
        obs_pic=pygame.image.load('car3.JPG')
    
    gameWindow.blit(obs_pic,(obs_startx,obs_starty))
    #gameWindow.blit(obs_pic,(obs_startx+random.randint(0,50),obs_starty+random.randint(0,50)))
def number_sys(passed,scroe):
    font=pygame.font.SysFont(None,25)
    text=font.render("PASSED :"+str(passed),True,white)
    scroe=font.render("SCORE :"+str(scroe),True,white)
    gameWindow.blit(text,(0,50))
    gameWindow.blit(scroe,(0,30))
   
def background():
    gameWindow.blit(gree,(0,0))
    gameWindow.blit(gree,(0,200))
    gameWindow.blit(gree,(0,400))
    gameWindow.blit(gree,(700,0))
    gameWindow.blit(gree,(700,200))
    gameWindow.blit(gree,(700,400))
    gameWindow.blit(ylw,(400,0))
    gameWindow.blit(ylw,(400,200))
    gameWindow.blit(ylw,(400,400))
    gameWindow.blit(whi,(110,0))
    gameWindow.blit(whi,(110,300))
    gameWindow.blit(whi,(680,0))
    gameWindow.blit(whi,(680,300))
    
def text_obj(text,font):
    textsurface=font.render(text,True,black)
    return textsurface ,textsurface.get_rect()

def message_disp(text):
    largertext=pygame.font.Font("freesansbold.ttf",65)
    rav,peet=text_obj(text,largertext)
    peet.center=((screen_width/2),(screen_height/2))
    gameWindow.blit(rav,peet)
    pygame.display.update()
    time.sleep(3)
    gameloop()
    
def out1():
    message_disp("YOU ARE OUT")

def car(x,y):
    gameWindow.blit(carimg,(x,y))

#varibels

def gameloop():
    x=(screen_width*0.45)
    y=(screen_height*0.8)
    x_c=0
    obs_speed=9
    obs=0
    obs_startx=random.randrange(140,(screen_width-140))
    obs_starty=-750
    obs_width=50
    obs_height=98
    passed=0
    score=0
    level=0
        
    exit_game = False
    while not exit_game:
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
      
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            x_c=5
                        
                        if event.key == pygame.K_LEFT:
                            x_c=-5
                        if event.key == pygame.K_a:
                            obs_speed+=4
                        
                        if event.key == pygame.K_b:
                            obs_speed-=4
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                            x_c=0
                                           
         x+= x_c              
         gameWindow.fill(white)
         background()
         obs_starty-=(obs_speed/8)
         obstical(obs_startx,obs_starty,obs)
         obs_starty+=obs_speed
         car(x,y)
         number_sys(passed,score)
         if x>678-car_wd or x<110:
           out1()  
         if x>screen_width-(obs_width+140) or x<140:
             out1
         if obs_starty>screen_height:
             obs_starty=0-obs_height
             obs_startx=random.randrange(145,(screen_width-145))
             obs=random.randrange(0,3)
             passed=passed+1
             score=score+10
             if int(passed)%10==0:
                 level=level+1
                 obs_speed+9
                 largertext=pygame.font.Font("freesansbold.ttf",65)
                 rav,peet=text_obj("LEVEL"+str(level),largertext)
                 peet.center=((screen_width/2),(screen_height/2))
                 gameWindow.blit(rav,peet)
                 pygame.display.update()
                 time.sleep(3)

         if y<obs_starty+obs_height:
             if x> obs_startx and x<obs_startx+obs_width or x+obs_width >obs_startx and x+obs_width<obs_startx+obs_width:
                 out1()
         pygame.display.update()
         clock.tick(40)

intro_bck()
gameloop()
pygame.quit()
quit()
            
   