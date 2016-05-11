import pygame

class teclas:  
    def display():
        display_width = 800
        display_height = 650        
        black = (0,0,0)
        white = (255,255,255)
        purple = (151,65,239)
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        guitarraImg = pygame.image.load('guitarra.png')
        guitarraImg = pygame.transform.scale(guitarraImg, (800,650))
        gameDisplay.fill(purple)
        gameDisplay.blit(guitarraImg, (0, 0))
        pygame.draw.line(gameDisplay, white ,[200,600], [600,600], 1)
        
        pygame.display.set_caption(('Bolinha descendo!'))
        
    def Score(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: "+str(count), True, black)
        gameDisplay.blit(text,(700,0))
        
        
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