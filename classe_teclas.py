import pygame

class teclas:  
    def __init__(self):
    self.gameDisplay.fill(purple)
    self.gameDisplay.blit(guitarraImg, (0, 0))
    self.pygame.draw.line(gameDisplay, white ,[200,600], [600,600], 1)
    
    def tecla1(x, y1):
        tecla1Img = pygame.image.load('botao1.png')
        tecla1Img = pygame.transform.scale(tecla1Img, (100,100))
        gameDisplay.blit(tecla1Img,(x,y1))
        
    def tecla2(x, y2):
        tecla2Img = pygame.image.load('botao2.png')
        tecla2Img = pygame.transform.scale(tecla2Img, (100,100))
        gameDisplay.blit(tecla2Img,( x+79 , y2))
     
    def tecla3(x, y3):
        tecla3Img = pygame.image.load('botao3.png')
        tecla3Img = pygame.transform.scale(tecla3Img, (100,100))
        gameDisplay.blit(tecla3Img,(x+158 , y3))
        
    def tecla4(x, y4):
        tecla4Img = pygame.image.load('botao4.png')
        tecla4Img = pygame.transform.scale(tecla4Img, (100,100))
        gameDisplay.blit(tecla4Img,(x+236 , y4))
    
    def tecla5(x, y5):
        tecla5Img = pygame.image.load('botao5.png')
        tecla5Img = pygame.transform.scale(tecla5Img, (100,100))
        gameDisplay.blit(tecla5Img,(x+316 , y5))