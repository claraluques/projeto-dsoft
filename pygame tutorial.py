#fazer tela tutorial
#criar função terminar jogo
#criar tela score final
#creditos + gifs?
#musicas
#botoes musicas
#TIRAR BAILE DA MUSICAS

import pygame
import classe_musicas as m
import classe_teclas as t

pygame.init()

pygame.mixer.init(44100, -16,2,2048)
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

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

FPS = 60

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('Guitar Student!'))

gameIcon = pygame.image.load('guitar_icon.png') #mudar icone
pygame.display.set_icon(gameIcon)

clock = pygame.time.Clock()
crashed = False

#movie = pygame.movie.Movie('fogoqueimando.mpeg')
#screen = pygame.display.set_mode(movie.get_size())
#movie_screen = pygame.Surface(movie.get_size()).convert()

gerente_imagens = t.GerenciadorImagens()

bg = pygame.image.load("fundofogo.png")

guitarraImg = pygame.image.load('guitarra.png')
guitarraImg = pygame.transform.scale(guitarraImg, (800,650))

escolhaImg = pygame.image.load('escolhamusica1.png')
escolhaImg = pygame.transform.scale(escolhaImg, (800,650))

pause = False

modo = -1 

PerfectImg = pygame.image.load('PERFECT.png')
PerfectImg = pygame.transform.scale(PerfectImg, (500,500))

VerygoodImg = pygame.image.load('VERY.GOOD.png')
VerygoodImg = pygame.transform.scale(VerygoodImg, (500,500))

GoodImg = pygame.image.load('GOOD.png')
GoodImg = pygame.transform.scale(GoodImg, (500,500))

MissedImg = pygame.image.load('MISSED.png')
MissedImg = pygame.transform.scale(MissedImg, (500,500))

   
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
    
def imagebutton(x,y,w,h,imagem1,imagem2,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        Imgbotao = pygame.image.load(imagem1)
        Imgbotao = pygame.transform.scale(Imgbotao, (w,h))
        gameDisplay.blit(Imgbotao,(x , y))
        
        if click[0] == 1 and action != None:
           action()      
    else:
       Img2botao = pygame.image.load(imagem2)
       Img2botao = pygame.transform.scale(Img2botao, (w,h))
       gameDisplay.blit(Img2botao,(x , y))
          

def sair_jogo():
    global intro, escolha
    escolha = "Sair"
    intro = False

def sair_jogo2():
    pygame.quit()
    quit()
    
def escolha_modo0(): #aleatorio
    global modo
    modo = 0
    loop_jogo()
    
def escolha_modo1(): #carry on my wayward
    global modo
    modo = 1
    loop_jogo()

def escolha_modo2(): #cliffs
    global modo
    modo = 2
    loop_jogo()
    
def escolha_modo3(): #house of gold
    global modo
    modo = 3
    loop_jogo()
    
def escolha_modo4(): #rolling in the deep
    global modo
    modo = 4
    loop_jogo()

def escolha_modo5(): #figure it out
    global modo
    modo = 5
    loop_jogo()
    
#def escolha_modo6(): 
#    global modo
#    modo = 6
#    loop_jogo()
#    
#def escolha_modo7(): 
#    global modo
#    modo = 7
#    loop_jogo()
#    
#def escolha_modo8():
#    global modo
#    modo = 8
#    loop_jogo()
#    
#def escolha_modo9():
#    global modo
#    modo = 9
#    loop_jogo()
    
def game_intro():
    global intro, Menu, FPS, movie, movie_screen, screen

    intro = True
#    movie.set_display(movie_screen)
#    movie.play()
    
    
    pygame.mixer.music.load('musicaintro.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.2) 
    
    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:

                quit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    Menu_musica()
                if event.key == pygame.K_ESCAPE:
                    quit()
        
#        screen.blit(movie_screen,(0,0))
        gameDisplay.fill(white)
#        gameDisplay.blit(bg, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Guitar Student", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
#        button("Quit",550,450,100,50,red,bright_red,sair_jogo2)
#        button("Jogar",150,450,100,50,green,bright_green,Menu_musica)        

        #button("Quit",550,450,100,50,red,bright_red,sair_jogo)
#        button("Quit",550,450,100,50,red,bright_red,sair_jogo)
#        imagebutton(500,450,200,100,'sair2.png','sair1.png',sair_jogo2)
#        imagebutton(100,450,200,100,'jogar2.png','jogar1.png',Menu_musica)
#        button("Jogar",150,450,100,50,green,bright_green,Menu_musica)        
        
        
        pygame.display.update()
        clock.tick(FPS)

    
        
def unpause():
        global pause
        pause = False
        pygame.mixer.music.unpause()
    
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
        pygame.mixer.music.pause()        
        
#        button("Continuar",150,450,100,50,green,bright_green,unpause)
        imagebutton(80,424,300,150,'continuar1.png', 'continuar2.png', unpause)

#        button("Menu",350,450,100,50,blue,bright_blue,game_intro)
        imagebutton(350,450,200,100,'menu1.png','menu2.png', game_intro)

#        button("Quit",550,450,100,50,red,bright_red,sair_jogo2)        
        imagebutton(500,450,200,100,'sair2.png','sair1.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)

def tela_final_muito_bom():
    while tela_final_muito_bom:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
                
      
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("YOU ROCK", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.mixer.music.pause()        
        

#        button("Menu",350,450,100,50,blue,bright_blue,game_intro)
        imagebutton(350,450,200,100,'menu1.png','menu2.png', game_intro)

#        button("Quit",550,450,100,50,red,bright_red,sair_jogo2)        
        imagebutton(500,450,200,100,'sair2.png','sair1.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)


def tela_final_bom():
    while tela_final_bom:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
                
      
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        pequenotexto = pygame.font.Font('freesansbold.ttf',25)
        TextSurf, TextRect = text_objects("YOU ROCK", largeText)
        TextSurf, TextRect = text_objects("a little", pequenotexto)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.mixer.music.pause()        
        

#        button("Menu",350,450,100,50,blue,bright_blue,game_intro)
        imagebutton(350,450,200,100,'menu1.png','menu2.png', game_intro)

#        button("Quit",550,450,100,50,red,bright_red,sair_jogo2)        
        imagebutton(500,450,200,100,'sair2.png','sair1.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)
def tela_fail():
    while tela_fail:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
                
      
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        pequenotexto = pygame.font.Font('freesansbold.ttf',25)
        TextSurf, TextRect = text_objects("Você falhou! " , largeText)
        TextSurf, TextRect = text_objects("seu ruim", pequenotexto)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.mixer.music.pause()        
        

#        button("Menu",350,450,100,50,blue,bright_blue,game_intro)
        imagebutton(350,450,200,100,'menu1.png','menu2.png', game_intro)

#        button("Quit",550,450,100,50,red,bright_red,sair_jogo2)        
        imagebutton(500,450,200,100,'sair2.png','sair1.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)

def Menu_musica():
    global Menu,escolha, intro

    escolha = ""
    
    Menu = True    
    intro = False
    
    altbot = 90
    largbot = 300
    coluna1 = 75
    coluna2 = 425
    espaco = 25
    
    while Menu:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
              
#        gameDisplay.fill(white)

#        largeText = pygame.font.Font('freesansbold.ttf',80)
#        TextSurf, TextRect = text_objects("Escolha sua musica", largeText)
#        TextRect.center = ((display_width/2),(display_height/2))
#        gameDisplay.blit(TextSurf, TextRect)
        
        gameDisplay.blit(escolhaImg, (0, 0))

#        button("Voltar",700,0,100,50,red,bright_red,game_intro)
#        button("GO!",150,450,100,50,green,bright_green,loop_jogo)
#        button("Voltar",450,450,100,50,red,bright_red,game_intro)
        imagebutton(display_width-190,570,180,90,'sair1.png','sair2.png', sair_jogo2)
#        button(blablabla,coluna1,100,largbot,altbot,green,bright_green, escolha_modo3)
        imagebutton(coluna1,(100+altbot+espaco),largbot,altbot,'rollinginthedeep2.png', 'rollinginthedeep1.png', escolha_modo4)
        imagebutton(coluna1,(100+2*(altbot+espaco)),largbot,altbot,'FiO1.png', 'FiO2.png', escolha_modo5)
#        imagebutton(coluna1,(100+3*(altbot+espaco)),largbot,altbot,'ComWS1.png', ' ComWS2.png', escolha_modo1)
        imagebutton(coluna2,350,largbot,altbot,'CoD2.png', 'CoD1.png', escolha_modo2)
        
        pygame.display.update()
        clock.tick(15)

    if escolha == "Go":
        loop_jogo2()
    elif escolha == "Sair":
        sair_jogo2()


def loop_jogo():
    global intro, escolha,Menu
    escolha = "Go"
    intro = False
    Menu = False
    
def loop_jogo2():    

    musica = m.musica(modo)
    listay1 = musica[0]
    listay2 = musica[1]
    listay3 = musica[2]
    listay4 = musica[3]
    listay5 = musica[4]
        
    x = 190
    
    count_perfect = -1
    count_verygood = -1
    count_good = -1
    count_missed = -1

    y_change = 5
    
    score = 0
    
    frames= 0
    
    crashed = False    
    
    while not crashed:
        global pause        
        
        gameDisplay.fill(purple)
        gameDisplay.blit(guitarraImg, (0, 0))
        pygame.draw.line(gameDisplay, white ,[200,600], [600,600], 1)
        bot(x,543,'buraco1.png')
        bot(x+79,543,'buraco2.png')
        bot(x+158,543,'buraco3.png')        
        bot(x+236,543,'buraco4.png')
        bot(x+316,543,'buraco5.png')
        
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
            musica = m.musica(modo)
            listay1 = musica[0]
            listay2 = musica[1]
            listay3 = musica[2]
            listay4 = musica[3]
            listay5 = musica[4]
            
        status = None
        
        
        for event in pygame.event.get():            
            if event.type == SONG_END:
                crashed = True
            if event.type == pygame.QUIT:
                crashed = True                
            if event.type == pygame.KEYDOWN:         
            
                if event.key == pygame.K_q:
                    for i in range (len(listay1)):
                        y1 = listay1[i]
                        score,status = t.process_key1(y1, score)
                        if status != None:
                            gerente_imagens.tecla1fogo(x,y1,gameDisplay)
                            break
                            
                elif event.key == pygame.K_w:
                    for i in range (len(listay2)):
                        y2 = listay2[i]
                        score,status = t.process_key2(y2, score)
                        if status != None:
                            gerente_imagens.tecla2fogo(x,y2,gameDisplay)
                            break
                        
                elif event.key == pygame.K_e:
                    for i in range (len(listay3)):
                        y3 = listay3[i]
                        score,status = t.process_key3(y3, score)
                        if status != None:
                            gerente_imagens.tecla3fogo(x,y3,gameDisplay)
                            break
                        
                elif event.key == pygame.K_r:
                    for i in range (len(listay4)):
                        y4 = listay4[i]
                        score,status = t.process_key4(y4, score)
                        if status != None:
                            gerente_imagens.tecla4fogo(x,y4,gameDisplay)
                            break
                                            
                elif event.key == pygame.K_t:
                    for i in range (len(listay5)):
                        y5 = listay5[i]
                        score,status = t.process_key5(y5, score)
                        if status != None:
                            gerente_imagens.tecla5fogo(x,y5,gameDisplay)
                            break
                        
                elif event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()                                        
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
        
        
        if status == "PERFECT":
            count_perfect = 0
        
        if status == "VERY GOOD":
            count_verygood = 0
            
        if status == "GOOD":
            count_good = 0
        
        if status == "MISSED":
            count_missed = 0
        
        
        if count_perfect >= 0:
            y1 = (900,900   )
            gameDisplay.blit(PerfectImg,(550,100))
            count_perfect += 1
            if count_perfect > 20:
                print("parei")
                count_perfect = -1
        
        if count_verygood >= 0:
                    gameDisplay.blit(VerygoodImg,(480,150))
                    count_verygood += 1
                    if count_verygood > 20:
                        print("parei")
                        count_verygood = -1
                        
        if count_good >= 0:
                    gameDisplay.blit(GoodImg,(450,175))
                    count_good += 1
                    if count_good > 20:
                        print("parei")
                        count_good = -1

        if count_missed >= 0:            
            gameDisplay.blit(MissedImg,(450,220))
            count_missed += 1
            if count_missed > 20:
                print("parei")
                count_missed = -1

        
        pygame.display.update()
        clock.tick(FPS)
        frames += 1
        
game_intro()
pygame.quit()
quit()