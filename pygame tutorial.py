import pygame
import classe_musicas as m
import classe_teclas as t

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
    elif d1 < 100:
        m.erro()
        print("MISSED")
#   elif y > 550: 
        
    return(score)

pygame.init()

pygame.mixer.init(44100, -16,2,2048)
#pygame.mixer.music.load(m.audio1())

display_width = 800
display_height = 650

blue = (0,0,255)
bright_blue = (0,0,200)
black = (0,0,0)
white = (255,255,255)
purple = (151,65,239)
red = (255,0,0)
bright_red = (200,0,0)
green = (0,255,0)
bright_green = (0,200,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('Guitar Student!'))
clock = pygame.time.Clock()
crashed = False

gerente_imagens = t.GerenciadorImagens()

guitarraImg = pygame.image.load('guitarra.png')
guitarraImg = pygame.transform.scale(guitarraImg, (800,650))

pause = False

modo = 0 #0: modo normal 1: modo aleatorio

#botoes = []
#for i in range(5):
#    filename = 'botao{0}.png'.format(i+1)
#    botaoImg = pygame.image.load(filename)
#    botaoImg = pygame.transform.scale(botaoImg, (100,100))
#    
#    botoes.append(botaoImg)

PerfectImg = pygame.image.load('Perfect.sprite.png')
PerfectImg = pygame.transform.scale(PerfectImg, (100,100))
   
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
#def bot1(x, y1):
#    gameDisplay.blit(bot1Img,(x,y1))
#
#def bot2(x, y2):
#    gameDisplay.blit(bot2Img,( x+79 , y2))
# 
#def bot3(x, y3):
#    gameDisplay.blit(bot3Img,(x+158 , y3))
#    
#def bot4(x, y4):
#    gameDisplay.blit(bot4Img,(x+236 , y4))
#
#def bot5(x, y5):
#    gameDisplay.blit(bot5Img,(x+316 , y5))
def bot(x,y,Img):
    botImg = pygame.image.load(Img)
    botImg = pygame.transform.scale(botImg, (100,100))
    gameDisplay.blit(botImg,(x , y))

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
    
def escolha_modo1():
    global modo
    modo = 0
    loop_jogo()

def escolha_modo2():
    global modo
    modo = 1
    loop_jogo()
    
def escolha_modo3():
    global modo
    modo = 2
    loop_jogo()
    
def game_intro():
    global intro, escolha

    intro = True
    escolha = ""
    
#    clock = pygame.time.Clock()
#    videointro = pygame.movie.Movie('.MPG')
#    screen = pygame.display.set_mode(videointro.get_size())
#    movie_screen = pygame.Surface(videointro.get_size()).convert()

#    videointro.set_display(movie_screen)
#    videointro.play()    
#    
    
    pygame.mixer.music.load('musicaintro.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.2) 
    
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
        
#        button("GO!",150,450,100,50,green,bright_green,loop_jogo)
        button("Quit",550,450,100,50,red,bright_red,sair_jogo)
        button("Baile",150,550,100,50,green,bright_green,escolha_modo1)        
        button("Aleatoria",450,550,100,50,green,bright_green,escolha_modo3)
        
        
        pygame.display.update()
        clock.tick(15)

    if escolha == "Go":
        loop_jogo2()
    else:
        sair_jogo2()
        

def unpause():
        global pause
        pause = False
        
    
def paused():
    while pause:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Menu",350,450,100,50,blue,bright_blue,game_intro)
        button("Quit",550,450,100,50,red,bright_red,sair_jogo2)        
        
        pygame.display.update()
        clock.tick(15)


def loop_jogo():
    global intro, escolha
    escolha = "Go"
    intro = False
    
    
def loop_jogo2():    
    ganhou = False

    musica1 = m.musica(modo)
    listay1 = musica1[0]
    listay2 = musica1[1]
    listay3 = musica1[2]
    listay4 = musica1[3]
    listay5 = musica1[4]

        
    x = (190)
    
    #y1 =random.randrange(-600,0)
    #y2 =random.randrange(-600,0)
    #y3 =random.randrange(-600,0)
    #y4 =random.randrange(-600,0)
    #y5 =random.randrange(-600,0)
    
    y_change = 5
    
    #xacerto1 = display_height*0.8
    #xacerto2 = display_height    
    
    score = 0
    
    frames= 0
    
    crashed = False    
    
#    videointro.stop()
    
    while not crashed:
        global pause        
        
        gameDisplay.fill(purple)
        gameDisplay.blit(guitarraImg, (0, 0))
        pygame.draw.line(gameDisplay, white ,[200,600], [600,600], 1)
        bot1 = bot(x,543,'buraco1.png')
        bot2 = bot(x+79,543,'buraco2.png')
        bot3 = bot(x+158,543,'buraco3.png')        
        bot4 = bot(x+236,543,'buraco4.png')
        bot5 = bot(x+316,543,'buraco5.png')
        
        Score(score)
        
        miny = display_height+50
        
        for i in range (len(listay1)):
            y1 = listay1[i]
            gerente_imagens.tecla1(x, y1, gameDisplay)       
            listay1[i] += y_change
            if y1 < miny:
                miny = y1
            
                
        for i in range (len(listay2)):
            y2 = listay2[i]
            gerente_imagens.tecla2(x, y2, gameDisplay)
            listay2[i] += y_change
            if y2 < miny:
                miny = y2

        for i in range (len(listay3)):
            y3 = listay3[i]
            gerente_imagens.tecla3(x, y3, gameDisplay)
            listay3[i] += y_change
            if y3 < miny:
                miny = y3
            
        for i in range (len(listay4)):
            y4 = listay4[i]
            gerente_imagens.tecla4(x, y4, gameDisplay)
            listay4[i] += y_change
            if y4 < miny:
                miny = y4
            
        for i in range (len(listay5)):
            y5 = listay5[i]
            gerente_imagens.tecla5(x, y5, gameDisplay)
            listay5[i] += y_change
            if y5 < miny:
                miny = y5
        
        if miny >= display_height:
            musica1 = m.musica(modo)
            listay1 = musica1[0]
            listay2 = musica1[1]
            listay3 = musica1[2]
            listay4 = musica1[3]
            listay5 = musica1[4]

     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True                
            if event.type == pygame.KEYDOWN:         
            
                if event.key == pygame.K_q:
                    for i in range (len(listay1)):
                        y1 = listay1[i]
                        score = process_key(y1, score)
                            
                elif event.key == pygame.K_w:
                    for i in range (len(listay2)):
                        y2 = listay2[i]
                        score = process_key(y2, score)
                        
                elif event.key == pygame.K_e:
                    for i in range (len(listay3)):
                        y3 = listay3[i]
                        score = process_key(y3, score)
                        
                elif event.key == pygame.K_r:
                    for i in range (len(listay4)):
                        y4 = listay4[i]
                        score = process_key(y4, score)
                                            
                elif event.key == pygame.K_t:
                    for i in range (len(listay5)):
                        y5 = listay5[i]
                        score = process_key(y5, score)
                elif event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()                                        
                    
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
        frames += 1
        
game_intro()
pygame.quit()
quit()