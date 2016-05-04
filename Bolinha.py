import pygame

class Bolinha:
    def __init__(self, y):
        self.y = y
        
    def bolinha_posicao1(self):
        self.bolinha1Img = pygame.image.load('botao1.png')
        self.bolinha1Img = pygame.transform.scale(self.bolinha1Img, (100,100))
        self.gameDisplay.blit(self.bolinha1Img,(190,y))
        
    def bolinha_posicao2(self, y):
        self.bolinha2Img = pygame.image.load('botao2.png')
        self.bolinha2Img = pygame.transform.scale(self.bolinha2Img, (100,100))
        self.gameDisplay.blit(self.bolinha2Img,(269,y))
        
    def bolinha_posicao3(self, y):
        self.bolinha3Img = pygame.image.load('botao3.png')
        self.bolinha3Img = pygame.transform.scale(self.bolinha3Img, (100,100))
        self.gameDisplay.blit(self.bolinha3Img,(348,y))
        
    def bolinha_posicao4(self, y):
        self.bolinha4Img = pygame.image.load('botao4.png')
        self.bolinha4Img = pygame.transform.scale(self.bolinha4Img, (100,100))
        self.gameDisplay.blit(self.bolinha4Img,(427,y))
        
    def bolinha_posicao5(self, y):
        self.bolinha5Img = pygame.image.load('botao5.png')
        self.bolinha5Img = pygame.transform.scale(self.bolinha5Img, (100,100))
        self.gameDisplay.blit(self.bolinha5Img,(506,y))