import pygame

class GerenciadorImagens:
    def __init__(self):
        self.tecla1Img = pygame.image.load('botao1.png')
        self.tecla1Img = pygame.transform.scale(self.tecla1Img, (100,100))
        
        self.tecla2Img = pygame.image.load('botao2.png')
        self.tecla2Img = pygame.transform.scale(self.tecla2Img, (100,100))
     
        self.tecla3Img = pygame.image.load('botao3.png')
        self.tecla3Img = pygame.transform.scale(self.tecla3Img, (100,100))
        
        self.tecla4Img = pygame.image.load('botao4.png')
        self.tecla4Img = pygame.transform.scale(self.tecla4Img, (100,100))
        
        self.tecla5Img = pygame.image.load('botao5.png')
        self.tecla5Img = pygame.transform.scale(self.tecla5Img, (100,100))
        
    def tecla1(self, x, y1, gameDisplay):
        gameDisplay.blit(self.tecla1Img,(x,y1))
        
    def tecla2(self, x, y2, gameDisplay):
        gameDisplay.blit(self.tecla2Img,( x+79 , y2))
     
    def tecla3(self, x, y3, gameDisplay):
        gameDisplay.blit(self.tecla3Img,(x+158 , y3))
        
    def tecla4(self, x, y4, gameDisplay):
        gameDisplay.blit(self.tecla4Img,(x+236 , y4))
    
    def tecla5(self, x, y5, gameDisplay):
        gameDisplay.blit(self.tecla5Img,(x+316 , y5))