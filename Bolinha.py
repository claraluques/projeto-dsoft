import pygame

class Bolinha:
    def __init__(self, y):
        self.y = y

    
    def posx(self, n, y):
        display_width = 800
        display_height = 600
        gameDisplay = pygame.display.set_mode((display_width, display_height))        

        x = 190
        if n == 0:
            x = x
            self.bolinha1Img = pygame.image.load('botao1.png')
            self.bolinha1Img = pygame.transform.scale(self.bolinha1Img, (100,100))
            gameDisplay.blit(self.bolinha1Img,(x,y))            
        elif n >= 1:
            x += 79*n
            if n == 1:
                self.bolinha2Img = pygame.image.load('botao2.png')
                self.bolinha2Img = pygame.transform.scale(self.bolinha2Img, (100,100))
                gameDisplay.blit(self.bolinha2Img,(x,y))
            elif n == 2:             
                self.bolinha3Img = pygame.image.load('botao3.png')
                self.bolinha3Img = pygame.transform.scale(self.bolinha3Img, (100,100))
                gameDisplay.blit(self.bolinha3Img,(348,y))               
            elif n == 3:
                self.bolinha4Img = pygame.image.load('botao4.png')
                self.bolinha4Img = pygame.transform.scale(self.bolinha4Img, (100,100))
                gameDisplay.blit(self.bolinha4Img,(427,y))
            elif n == 4:
                self.bolinha5Img = pygame.image.load('botao5.png')
                self.bolinha5Img = pygame.transform.scale(self.bolinha5Img, (100,100))
                gameDisplay.blit(self.bolinha5Img,(506,y))               


            
  