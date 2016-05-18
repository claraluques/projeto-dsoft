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
        
        
#Definindo funções para verificar o acerto dos botões de cada coluna

def process_key1(y1, score):
    d1 = y1 - 550
    if d1 < 5:
        print('PERFECT')
        score +=3
        print("SCORE: {0}".format(score))
    elif d1 < 15:
        print ("VERY GOOD")
        score += 2
        print("SCORE: {0}".format(score))
    elif d1 < 25:
        print ("GOOD")
        score += 1
        print("SCORE: {0}".format(score))                   
    elif d1 < 100:
        m.erro()
        print("MISSED")
    return score
    
def process_key2(y2, score):
    d2 = y2 - 550
    if d2 < 5:
        print('PERFECT')
        score +=3
        print("SCORE: {0}".format(score))
    elif d2 < 15:
        print ("VERY GOOD")
        score += 2
        print("SCORE: {0}".format(score))
    elif d2 < 25:
        print ("GOOD")
        score += 1
        print("SCORE: {0}".format(score))                   
    elif d2 < 100:
        m.erro()
        print("MISSED")
    return score
    
def process_key3(y3, score):
    d3 = y3 - 550
    if d3 < 5:
        print('PERFECT')
        score +=3
        print("SCORE: {0}".format(score))
    elif d3 < 15:
        print ("VERY GOOD")
        score += 2
        print("SCORE: {0}".format(score))
    elif d3 < 25:
        print ("GOOD")
        score += 1
        print("SCORE: {0}".format(score))                   
    elif d3 < 100:
        m.erro()
        print("MISSED")
    return score
    
def process_key4(y4, score):
    d4 = y4 - 550
    if d4 < 5:
        print('PERFECT')
        score +=3
        print("SCORE: {0}".format(score))
    elif d4 < 15:
        print ("VERY GOOD")
        score += 2
        print("SCORE: {0}".format(score))
    elif d4 < 25:
        print ("GOOD")
        score += 1
        print("SCORE: {0}".format(score))                   
    elif d4 < 100:
        m.erro()
        print("MISSED")
    return score
    
def process_key5(y5, score):
    d5 = y5 - 550
    if d5 < 5:
        print('PERFECT')
        score +=3
        print("SCORE: {0}".format(score))
    elif d5 < 15:
        print ("VERY GOOD")
        score += 2
        print("SCORE: {0}".format(score))
    elif d5 < 25:
        print ("GOOD")
        score += 1
        print("SCORE: {0}".format(score))                   
    elif d5 < 100:
        m.erro()
        print("MISSED")
    return score