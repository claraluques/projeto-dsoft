import pygame
import random
from classe_musicas import musicas as m
from classe_teclas import teclas as t


pygame.init()

display_width = 800
display_height = 650

black = (0,0,0)
white = (255,255,255)
purple = (151,65,239)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('Bolinha descendo!'))
clock = pygame.time.Clock()
crashed = False

guitarraImg = pygame.image.load('guitarra.png')
guitarraImg = pygame.transform.scale(guitarraImg, (800,650))

def Score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(700,0))

ganhou = False

x = (190)

musica1 = m.musica_1()
print (musica1)

for nota in range (len(musica1)):
    x = -600
    if nota == 0:
        y1 = -600
    elif nota == 1:
        y2 = (x-100*nota)
    elif nota == 2:
        y3 = (x-100*nota)
    elif nota == 3:
        y4 = (x-100*nota)
    elif nota == 4:
        y5 = (x-100*nota)

y_change = 0

area_de_acerto = display_height - 500 

xacerto1 = display_height*0.8
xacerto2 = display_height

score = 0

while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                y_change = 5
                
            elif event.key == pygame.K_UP:
               y_change = -5
               
            elif event.key == pygame.K_q:
                d1 = y1-550
                if d1 < 0:
                    d1 = -d1
                if d1 < 5:
                    print('PERFECT')
#                    y1=random.randrange(-600,0)
                    score +=3
                    print("SCORE: {0}".format(score))
                elif d1 < 15:
                    print ("VERY GOOD")
                    score += 2
                    print("SCORE: {0}".format(score))
#                    y1 =random.randrange(-600,0)
                elif d1 < 25:
                    print ("GOOD")
                    score += 1
                    print("SCORE: {0}".format(score))
#                    y1 =random.randrange(-600,0)                    
                    
                else:
                    print("MISSED")
                    
            elif event.key == pygame.K_w:
                d2 = y2-550
                if d2 < 0:
                    d2 = -d2
                if d2 < 5:
                    print('PERFECT')
                    score += 3
                    print("SCORE: {0}".format(score))
#                    y2 =random.randrange(-600,0)
                elif d2 < 25:
                    print ("VERY GOOD")
                    score += 2
                    print("SCORE: {0}".format(score))
#                    y2 =random.randrange(-600,0)
                elif d2 < 25:
                    print ("GOOD")
                    score += 1
                    print("SCORE: {0}".format(score))
#                    y2 =random.randrange(-600,0)                    
                else:
                    print("MISSED")
                    
            elif event.key == pygame.K_e:
                d3 = y3-550
                if d3 < 0:
                    d3 = -d3
                if d3 < 5:
                    print('PERFECT')
                    score += 3
                    print("SCORE: {0}".format(score))
#                    y3 =random.randrange(-600,0)
                elif d3 < 25:
                    print ("VERY GOOD")
                    score += 2
                    print("SCORE: {0}".format(score))
#                    y3 =random.randrange(-600,0)
                elif d3 < 25:
                    print ("GOOD")
                    score += 1
                    print("SCORE: {0}".format(score))
#                    y3 =random.randrange(-600,0) 
                else:
                    print("MISSED")
                    
            elif event.key == pygame.K_r:
                d4 = y4-550
                if d4 < 0:
                    d4 = -d4
                if d4 < 5:
                    print('PERFECT')
                    score += 3
                    print("SCORE: {0}".format(score))
#                    y4 =random.randrange(-600,0)
                elif d4 < 25:
                    print ("VERY GOOD")
                    score += 2
                    print("SCORE: {0}".format(score))
#                    y4 =random.randrange(-600,0)
                elif d4 < 25:
                    print ("GOOD")
                    score += 1
                    print("SCORE: {0}".format(score))
#                    y4 =random.randrange(-600,0)                 
                else:
                    print("MISSED")
                    
                    
            elif event.key == pygame.K_t:
                d5 = y5-550
                if d5 < 0:
                    d5 = -d5
                if d5 < 5:
                    print('PERFECT')
                    score += 3
                    print("SCORE: {0}".format(score))
#                    y5 =random.randrange(-600,0)
                elif d5 < 25:
                    print ("VERY GOOD")
                    score += 2
                    print("SCORE: {0}".format(score))
#                    y5 =random.randrange(-600,0)
                elif d5 < 25:
                    print ("GOOD")
                    score += 1
                    print("SCORE: {0}".format(score))
#                    y5 =random.randrange(-600,0)                
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
    pygame.draw.line(gameDisplay, white ,[200,600], [600,600], 1)
    
    Score(score)   
    
    t.tecla1(x, y1)
    t.tecla2(x, y2)
    t.tecla3(x, y3)    
    t.tecla4(x, y4)
    t.tecla5(x, y5)
    
#    if y1 > display_height:
#        y1 = random.randrange(-200,0) 
#        
#    if y2 > display_height:
#        y2 = random.randrange(-100,0)
#        
#    if y3 > display_height:
#        y3 = random.randrange(-400,0)
#        
#    if y4 > display_height:
#        y4 = random.randrange(-250,0)
#        
#    if y5 > display_height:
#        y5 = random.randrange(-300,0)
    
    if score == 100:
        ganhou = True
    if ganhou == True:
        crashed = True
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()