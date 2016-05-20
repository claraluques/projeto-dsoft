#import os
#os.environ['SDL_VIDEODRIVER'] = 'windib'
import pygame
import classe_musicas as m
import classe_teclas as t

pygame.init()

pygame.mixer.init(44100, -16,2,2048)

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

gameIcon = pygame.image.load('icone.png') #mudar icone
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

pause = False

modo = -1 

PerfectImg = pygame.image.load('Perfect.sprite.png')
PerfectImg = pygame.transform.scale(PerfectImg, (100,100))
   
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
#                movie.stop()
#                pygame.quit()
                quit()

        


        
#        screen.blit(movie_screen,(0,0))
        gameDisplay.fill(white)
#        gameDisplay.blit(bg, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf',100)

        TextSurf, TextRect = text_objects("Guitar Student", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        #button("Quit",550,450,100,50,red,bright_red,sair_jogo)
#        button("Quit",550,450,100,50,red,bright_red,sair_jogo)
        imagebutton(500,450,200,100,'sair2.png','sair1.png',sair_jogo)
        imagebutton(100,450,200,100,'jogar2.png','jogar1.png',Menu_musica)
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
        
        button("Continuar",150,450,100,50,green,bright_green,unpause)
#        button("Menu",350,450,100,50,blue,bright_blue,game_intro)
        imagebutton(350,450,200,100,'menu1.png','menu2.png', game_intro)

        button("Quit",550,450,100,50,red,bright_red,sair_jogo2)        
        
        pygame.display.update()
        clock.tick(15)

def Menu_musica():
    global Menu,escolha

    escolha = ""
    Menu = True    
    
    while Menu:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
              
        gameDisplay.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Escolha sua musica", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
#        button("GO!",150,450,100,50,green,bright_green,loop_jogo)
#        button("Voltar",450,450,100,50,red,bright_red,game_intro)
        imagebutton(display_width-200,0,200,100,'voltar1.png','voltar2.png', game_intro)
        button("Baile",150,550,100,50,green,bright_green,escolha_modo1)        
        button("Aleatoria",450,550,100,50,green,bright_green,escolha_modo3)
        
        
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
    ganhou = False

    musica = m.musica(modo)
    listay1 = musica[0]
    listay2 = musica[1]
    listay3 = musica[2]
    listay4 = musica[3]
    listay5 = musica[4]
        
    x = (190)

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
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True                
            if event.type == pygame.KEYDOWN:         
            
                if event.key == pygame.K_q:
                    for i in range (len(listay1)):
                        y1 = listay1[i]
                        score = t.process_key1(y1, score)
                            
                elif event.key == pygame.K_w:
                    for i in range (len(listay2)):
                        y2 = listay2[i]
                        score = t.process_key2(y2, score)
                        
                elif event.key == pygame.K_e:
                    for i in range (len(listay3)):
                        y3 = listay3[i]
                        score = t.process_key3(y3, score)
                        
                elif event.key == pygame.K_r:
                    for i in range (len(listay4)):
                        y4 = listay4[i]
                        score = t.process_key4(y4, score)
                                            
                elif event.key == pygame.K_t:
                    for i in range (len(listay5)):
                        y5 = listay5[i]
                        score = t.process_key5(y5, score)
                        
                elif event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()                                        
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
    
        if score == 100:
            ganhou = True
        if ganhou == True:
            crashed = True
        
        pygame.display.update()
        clock.tick(FPS)
        frames += 1
        
game_intro()
pygame.quit()
quit()