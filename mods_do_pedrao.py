import pygame
import random
from classe_musicas import musicas as m

def process_key(y, score):
    d1 = y - 550
    if d1 < 0:
        d1 = -d1
    if d1 < 5:
        print('PERFECT')
        Perfect(650,100)
#        y = random.randrange(-600,0)
        score +=3
        print("SCORE: {0}".format(score))
        
    elif d1 < 15:
        print ("VERY GOOD")
        score += 2
        print("SCORE: {0}".format(score))
#        y =random.randrange(-600,0)
    elif d1 < 25:
        print ("GOOD")
        score += 1
        print("SCORE: {0}".format(score))
#        y = random.randrange(-600,0)                    
    else:
        print("MISSED")
        
    return (y, score)

pygame.init()

display_width = 800
display_height = 650

black = (0,0,0)
white = (255,255,255)
purple = (151,65,239)
red = (255,0,0)
bright_red = (200,0,0)
green = (0,255,0)
bright_green = (0,200,0)




gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('Bolinha descendo!'))
clock = pygame.time.Clock()
crashed = False

pygame.image.load

guitarraImg = pygame.image.load('guitarra.png')
guitarraImg = pygame.transform.scale(guitarraImg, (800,650))

#botoes = []
#for i in range(5):
#    filename = 'botao{0}.png'.format(i+1)
#    botaoImg = pygame.image.load(filename)
#    botaoImg = pygame.transform.scale(botaoImg, (100,100))
#    
#    botoes.append(botaoImg)
 

PerfectImg = pygame.image.load('Perfect.sprite.png')
PerfectImg = pygame.transform.scale(PerfectImg, (100,100))

   
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

#def bot(i, x, y):
#    gameDisplay.blit(botoes[i], (x,y))

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

def Score(count):
    font = pygame.font.SysFont(None,40)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(650,0))    

def Perfect(x, y):
    gameDisplay.blit(PerfectImg ,(650, 200))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
           action()      
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def sair_jogo():
    global intro, escolha
    escolha = "Sair"
    intro = False

def sair_jogo2():
    pygame.quit()
    quit()


def game_intro():
    global intro, escolha

    intro = True
    escolha = ""

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Guitar Student", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!",150,450,100,50,green,bright_green,loop_jogo)
        button("Quit",550,450,100,50,red,bright_red,sair_jogo)        
        
        pygame.display.update()
        clock.tick(15)

    if escolha == "Go":
        loop_jogo2()
    else:
        sair_jogo2()



def loop_jogo():
    global intro, escolha
    escolha = "Go"
    intro = False
    
def loop_jogo2():

    ganhou = False
        
    musica1 = m.musica1()
    listay1 = musica1[0]
    listay2 = musica1[1]
    listay3 = musica1[2]
    listay4 = musica1[3]
    listay5 = musica1[4]
    
    
    
    x = 190
    
    #y1 =random.randrange(-600,0)
    #y2 =random.randrange(-600,0)
    #y3 =random.randrange(-600,0)
    #y4 =random.randrange(-600,0)
    #y5 =random.randrange(-600,0)
    y_change = 0
    
    
    
    
    
    #xacerto1 = display_height*0.8
    #xacerto2 = display_height
    
    
    score = 0
    
    
    
    crashed = False    
    
    while not crashed:
        
        gameDisplay.fill(purple)
        gameDisplay.blit(guitarraImg, (0, 0))
        pygame.draw.line(gameDisplay, white ,[200,600], [600,600], 1)
        
    
        Score(score)
    
        for i in range (len(listay1)):
            y1 = listay1[i]
            bot1(x, y1)        
            listay1[i] += y_change
        for i in range (len(listay2)):
            y2 = listay2[i]
            bot2(x, y2)
            listay2[i] += y_change
        for i in range (len(listay3)):
            y3 = listay3[i]
            bot3(x, y3)
            listay3[i] += y_change
        for i in range (len(listay4)):
            y4 = listay4[i]
            bot4(x, y4)
            listay4[i] += y_change
        for i in range (len(listay5)):
            y5 = listay5[i]
            bot5(x, y5)
            listay5[i] += y_change  
        
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    y_change = 5
                    
                elif event.key == pygame.K_UP:
                    y_change = -5
                   
                elif event.key == pygame.K_q:
                    y1, score = process_key(y1, score)
                        
                elif event.key == pygame.K_w:
                    y2, score = process_key(y2, score)
                        
                elif event.key == pygame.K_e:
                    y3, score = process_key(y3, score)
                        
                elif event.key == pygame.K_r:
                    y4, score = process_key(y4, score)
                                            
                elif event.key == pygame.K_t:
                    y5, score = process_key(y5, score)
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        

    
    
    

    
    

#    bot1(x, y1)
#    bot2(x, y2)
#    bot3(x, y3)    
#    bot4(x, y4)
#    bot5(x, y5)
       
       
    
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
    
    
game_intro()    
    
    
pygame.quit()
quit()