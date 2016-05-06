import pygame
import random

pygame.init()

display_width = 800
display_height = 600


white = (255,255,255)
purple = (151,65,239)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('Bolinha descendo!'))
clock = pygame.time.Clock()
crashed = False


guitarraImg = pygame.image.load('guitarra.png')
guitarraImg = pygame.transform.scale(guitarraImg, (800,600))


bot1Img = pygame.image.load('botao1.png')
bot1Img = pygame.transform.scale(bot1Img, (100,100))

bot2Img = pygame.image.load('botao2.png')
bot2Img = pygame.transform.scale(bot2Img, (100,100))

bot3Img = pygame.image.load('botao3.png')
bot3Img = pygame.transform.scale(bot3Img, (100,100))

bot4Img = pygame.image.load('botao4.png')
bot4Img = pygame.transform.scale(bot4Img, (100,100))

bot5Img = pygame.image.load('botao5.png')
bot5Img = pygame.transform.scale(bot5Img, (100,100))



def bot1(x, y1):
    gameDisplay.blit(bot1Img,(x,y1))

def bot2(x, y2):
    gameDisplay.blit(bot2Img,( x+79 , y2))
 
def bot3(x, y3):
    gameDisplay.blit(bot3Img,(x+158 , y3))
    
def bot4(x, y4):
    gameDisplay.blit(bot4Img,(x+236 , y4))

def bot5(x, y5):
    gameDisplay.blit(bot5Img,(x+316 , y5))






x = (190)

y1 =random.randrange(-600,0)
y2 =random.randrange(-600,0)
y3 =random.randrange(-600,0)
y4 =random.randrange(-600,0)
y5 =random.randrange(-600,0)
y_change = 0




area_de_acerto = display_height - 500 

xacerto1 = display_height*0.8
xacerto2 = display_height

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                y_change = 5
            elif event.key == pygame.K_UP:
               y_change = -5
            elif event.key == pygame.K_a:
                d = y1-550
                if d < 0:
                    d = -d
                if d < 5:
                    print('PERFECT')
                elif d < 25:
                    print ("VERY GOOD")
                else:
                    print("MISSED")
                
            
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
    
    
            

        
    y1 += y_change
    y2 += y_change
    y3 += y_change
    y4 += y_change
    y5 += y_change
    

    
    gameDisplay.fill(purple)
    gameDisplay.blit(guitarraImg, (0, 0))
    

#    bolinha1 = Bolinha(y)
#    bolinha1.posx(0,y)

        
    bot1(x, y1)
    bot2(x, y2)
    bot3(x, y3)    
    bot4(x, y4)
    bot5(x, y5)
    
    if y1 > display_height:
        y1 = random.randrange(-200,0) 
        
    if y2 > display_height:
        y2 = random.randrange(-100,0)
        
    if y3 > display_height:
        y3 = random.randrange(-400,0)
        
    if y4 > display_height:
        y4 = random.randrange(-250,0)
        
    if y5 > display_height:
        y5 = random.randrange(-300,0)
    
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()