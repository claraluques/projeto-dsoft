import pygame
import Bolinha

pygame.init()

display_width = 800
display_height = 600


black = (0,0,0)
white = (255,255,255)
purple = (151,65,239)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('Bolinha descendo!'))
clock = pygame.time.Clock()
crashed = False


#
#bot1Img = pygame.image.load('botao1.png')
#bot1Img = pygame.transform.scale(bot1Img, (100,100))
#
#bot2Img = pygame.image.load('botao2.png')
#bot2Img = pygame.transform.scale(bot2Img, (100,100))
#
#bot3Img = pygame.image.load('botao3.png')
#bot3Img = pygame.transform.scale(bot3Img, (100,100))
#
#bot4Img = pygame.image.load('botao4.png')
#bot4Img = pygame.transform.scale(bot4Img, (100,100))
#
#bot5Img = pygame.image.load('botao5.png')
#bot5Img = pygame.transform.scale(bot5Img, (100,100))
#
guitarraImg = pygame.image.load('guitarra.png')
guitarraImg = pygame.transform.scale(guitarraImg, (800,600))

#def bot1(x, y):
#    gameDisplay.blit(bot1Img,(x,y))
#
#def bot2(x, y):
#    gameDisplay.blit(bot2Img,( x+79 , y-100))
# 
#def bot3(x, y):
#    gameDisplay.blit(bot3Img,(x+158 , y-50))
#    
#def bot4(x, y):
#    gameDisplay.blit(bot4Img,(x+236 , y+20))
#
#def bot5(x, y):
#    gameDisplay.blit(bot5Img,(x+316 , y+100))
#
#x = (190)

y = (display_height*0.2)
y_change = 0


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                y_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
    
        
    bolinha1 = Bolinha(y)
    bolinha1.bolinha_posicao1()
        
    y += y_change
    

    
    gameDisplay.fill(purple)
    gameDisplay.blit(guitarraImg, (0, 0))
    
#    bot1(x, y)
#    bot2(x, y)
#    bot3(x, y)    
#    bot4(x, y)
#    bot5(x, y)
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()