#creditos + gifs?
#as frases e palavras do jogo esta metade em ingles e metade em portugues!!


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

altbot = 90
largbot = 300

coluna1 = 75
coluna2 = 425

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('GUITARPIXEL!'))

gameIcon = pygame.image.load('guitar_icon.png') #mudar icone
pygame.display.set_icon(gameIcon)

clock = pygame.time.Clock()
crashed = False

gerente_imagens = t.GerenciadorImagens()

bg = pygame.image.load("fundofogo.png")

guitarraImg = pygame.image.load('guitarra2.png')
guitarraImg = pygame.transform.scale(guitarraImg, (800,650))

escolhaImg = pygame.image.load('escolhamusica.png')
escolhaImg = pygame.transform.scale(escolhaImg, (800,650))

tutorialImg = pygame.image.load('tutorial.png')
tutorialImg = pygame.transform.scale(tutorialImg, (800,650))

introImg = pygame.image.load('pressioneespaco.png')
introImg = pygame.transform.scale(introImg, (800,650))

creditoImg = pygame.image.load('creditos.png')
creditoImg = pygame.transform.scale(creditoImg, (800,650))

pausadoImg = pygame.image.load('pausado.png')
pausadoImg = pygame.transform.scale(pausadoImg,(800,650))

yourockImg = pygame.image.load('yourock.png')
yourockImg = pygame.transform.scale(yourockImg,(800,650))

yourockalittleImg = pygame.image.load('yourockalittle.png')
yourockalittleImg = pygame.transform.scale(yourockalittleImg,(800,650))

seulixoImg = pygame.image.load('seulixo.png')
seulixoImg = pygame.transform.scale(seulixoImg,(800,650))

PerfectImg = pygame.image.load('PERFECT.png')
PerfectImg = pygame.transform.scale(PerfectImg, (500,500))

VerygoodImg = pygame.image.load('VERY.GOOD.png')
VerygoodImg = pygame.transform.scale(VerygoodImg, (500,500))

GoodImg = pygame.image.load('GOOD.png')
GoodImg = pygame.transform.scale(GoodImg, (500,500))

MissedImg = pygame.image.load('MISSED.png')
MissedImg = pygame.transform.scale(MissedImg, (500,500))

pause = False
tutorial = False
credito = False

modo = -1 

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

def escolha_modo2(): #cliffs of dover
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
    
def escolha_modo6(): #bohemian rhapsody
    global modo
    modo = 6
    loop_jogo()
    
#FUNÇÕES PARA FUTURAS IMPLEMENTAÇÕES DE MÚSICAS    

#def escolha_modo7(): 
#    global modo
#    modo = 7
#    loop_jogo()
    
#def escolha_modo8():
#    global modo
#    modo = 8
#    loop_jogo()
   
#def escolha_modo9():
#    global modo
#    modo = 9
#    loop_jogo()
   
def game_tutorial():
    global tutorial, Menu, FPS, tutorialImg

    tutorial = True
    
    while tutorial:
        
        gameDisplay.blit(tutorialImg,(0 , 0))
             
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_z:
                    game_intro()

                if event.key == pygame.K_ESCAPE:
                    quit()

        pygame.display.update()
        
def game_creditos():
    global tutorial, Menu, FPS, creditolImg

    credito = True
    
    while credito:
        
        gameDisplay.blit(creditoImg,(0 , 0))
             
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_z:
                    game_intro()

                if event.key == pygame.K_ESCAPE:
                    quit()

        pygame.display.update()
    
def game_intro():
    global intro, Menu, FPS, tutorial, introImg
    
    intro = True
    tutorial = False
    credito = False
      
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

                if event.key == pygame.K_a:
                    game_tutorial()
                    
                if event.key == pygame.K_s:
                    game_creditos()
                    
                if event.key == pygame.K_ESCAPE:
                    quit()

        gameDisplay.blit(introImg,(0 , 0))
        

        
        pygame.display.update()
        clock.tick(FPS)    
        
def unpause():
        global pause
        pause = False
        pygame.mixer.music.unpause()
    
def paused():
    global altbot, largbot
    while pause:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()                    
      
        gameDisplay.blit(pausadoImg,(0 , 0))
           
        pygame.mixer.music.pause()        
        
        imagebutton(250,310,largbot,altbot,'continuar1.png', 'continuar2.png', unpause)
        imagebutton(250,410,largbot, altbot,'menu1.png','menu2.png', game_intro)
        imagebutton(250,510,largbot,altbot,'sair1.png','sair2.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)

def tela_final_muito_bom():
    global altbot, largbot, coluna1, coluna2, gameDisplay
    
    while tela_final_muito_bom:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()          
        
        gameDisplay.blit(yourockImg,(0 , 0))
        
        
        pygame.mixer.music.pause()        

        imagebutton(coluna1,450,largbot,altbot,'menu1.png','menu2.png', game_intro)
        imagebutton(coluna2,450,largbot,altbot,'sair1.png','sair2.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)


def tela_final_bom():
    global altbot, largbot, coluna1, coluna2, gameDisplay
        
    while tela_final_bom:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(yourockalittleImg,(0,0))
        
        pygame.mixer.music.pause()        
        
        imagebutton(coluna1,450,largbot,altbot,'menu1.png','menu2.png', game_intro)
        imagebutton(coluna2,450,largbot,altbot,'sair1.png','sair2.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)
        
def tela_fail():
    global altbot, largbot, coluna1, coluna2, gameDisplay
    
    while tela_fail:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(seulixoImg,(0,0))

        pygame.mixer.music.pause()        

        imagebutton(coluna1,450,largbot,altbot,'menu1.png','menu2.png', game_intro)
        imagebutton(coluna2,450,largbot,altbot,'sair1.png','sair2.png',sair_jogo2)
        
        pygame.display.update()
        clock.tick(15)

def get_high_score():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score
 
 
def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")
 
 
def main():
    """ Main program is here. """
    # Get the high score
    high_score = get_high_score()
 
    # Get the score from the current game
    score1 = 0
    try:
        # Ask the user for his/her score
        score1 = score
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")
 
    # See if we have a new high score
    if score1 > high_score:
        # We do! Save to disk
        print("Yea! New high score!")
        save_high_score(score1)
    else:
        print("Better luck next time.")        

def Menu_musica():
    global Menu,escolha, intro, score, altbot, largbot, coluna1, coluna2

    escolha = ""
    
    Menu = True    
    intro = False
    


    espaco = 25
    score = 0
    
    while Menu:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
              
        gameDisplay.blit(escolhaImg, (0, 0))

        imagebutton(coluna1,550,largbot,altbot,'voltar2.png','voltar1.png',game_intro)     
        imagebutton(coluna2,550,largbot,altbot,'sair1.png','sair2.png',sair_jogo2)

        imagebutton(coluna1,(100+altbot+espaco),largbot,altbot,'rollinginthedeep2.png', 'rollinginthedeep1.png', escolha_modo4)
        imagebutton(coluna1,(100+2*(altbot+espaco)),largbot,altbot,'FiO1.png', 'FiO2.png', escolha_modo5)
        imagebutton(coluna2,(100+1*(altbot+espaco)),largbot,altbot,'HoG1.png', 'HoG2.png', escolha_modo3)        
#        imagebutton(coluna1,(100+3*(altbot+espaco)),largbot,altbot,'ComWS1.png', 'ComWS2.png', escolha_modo1)
        imagebutton(coluna2,(100+2*(altbot+espaco)),largbot,altbot,'CoD2.png', 'CoD1.png', escolha_modo2)
#        imagebutton(coluna2,(100+3*(altbot+espaco)),largbot,altbot,'BR2.png', 'BR1.png', escolha_modo6)
        
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
    tamanho = musica[5]
        
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
        
        porcen = score/tamanho
        if miny >= display_height:
            if porcen > 2:
                tela_final_muito_bom()
            elif porcen > 1:
                tela_final_bom()
            else:
                tela_fail()

        status = None
        
        
        for event in pygame.event.get():            
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