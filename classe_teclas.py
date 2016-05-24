import pygame
import classe_musicas as m

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
        
        self.tecla1fogoImg = pygame.image.load('bolinha.flamejante1.png')
        self.tecla1fogoImg = pygame.transform.scale(self.tecla1fogoImg, (100,100))
        
        self.tecla2fogoImg = pygame.image.load('bolinha.flamejante2.png')
        self.tecla2fogoImg = pygame.transform.scale(self.tecla2fogoImg, (100,100))
        
        self.tecla3fogoImg = pygame.image.load('bolinha.flamejante3.png')
        self.tecla3fogoImg = pygame.transform.scale(self.tecla3fogoImg, (100,100))

        self.tecla4fogoImg = pygame.image.load('bolinha.flamejante4.png')
        self.tecla4fogoImg = pygame.transform.scale(self.tecla4fogoImg, (100,100))
        
        self.tecla5fogoImg = pygame.image.load('bolinha.flamejante5.png')
        self.tecla5fogoImg = pygame.transform.scale(self.tecla5fogoImg, (100,100))
        
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
        
    def tecla1fogo(self, x, y1, gameDisplay):
        gameDisplay.blit(self.tecla1fogoImg,(x , y1))
        
    def tecla2fogo(self, x, y2, gameDisplay):
        gameDisplay.blit(self.tecla2fogoImg,(x+79 , y2))

    def tecla3fogo(self, x, y3, gameDisplay):
        gameDisplay.blit(self.tecla3fogoImg,(x+158 , y3))

    def tecla4fogo(self, x, y4, gameDisplay):
        gameDisplay.blit(self.tecla4fogoImg,(x+236 , y4))
        
    def tecla5fogo(self, x, y5, gameDisplay):
        gameDisplay.blit(self.tecla5fogoImg,(x+316 , y5))
        
#Definindo funções para verificar o acerto dos botões de cada coluna

def process_key(y, score):
    d = y - 550
    if d < 0:
        d = -d
        
    status = None
    if d < 5:
        print('PERFECT')
        score +=3
        status = "PERFECT"
        print("SCORE: {0}".format(score))
    elif d < 15:
        print ("VERY GOOD")
        score += 2
        status = "VERY GOOD"
        print("SCORE: {0}".format(score))
    elif d < 25:
        print ("GOOD")
        score += 1
        status = "GOOD"
        print("SCORE: {0}".format(score))                   
    elif d < 200:
        m.erro()
        print("MISSED")
    return score, status


def process_key1(y1, score):
    return process_key(y1, score)
    
def process_key2(y2, score):
    return process_key(y2, score)

def process_key3(y3, score):
    return process_key(y3, score)
    
def process_key4(y4, score):
    return process_key(y4, score)
    
def process_key5(y5, score):
    return process_key(y5, score)
    