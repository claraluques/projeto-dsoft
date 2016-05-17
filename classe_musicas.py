import pygame
import random
def erro():

    sound = pygame.mixer.Sound("erro.ogg")
    sound.set_volume(0.4)
    sound.play(loops = 0)
            
def musica1():
    pygame.mixer.music.load('baile.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.2)
    
    oimusica1 = open('baile.txt', 'r')
    musica1txt = oimusica1.readlines()
    oimusica1.close()
    musica1str = list(musica1txt[0])
    musica1 = []
    for i in range (len(musica1str)):
        musica1.append(int(musica1str[i]))
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    for i in range (len(musica1)):
        if musica1[i] == 0:
            y1.append(-100*i)
        elif musica1[i] == 1:
            y2.append(-100*i)
        elif musica1[i] == 2:
            y3.append(-100*i)
        elif musica1[i] == 3:
            y4.append(-100*i)
        elif musica1[i] == 4:
            y5.append(-100*i)
    return y1, y2, y3, y4, y5
    
def musicaale():
    nbolinhas = 5
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    for i in range (nbolinhas):
        c = random.randint(0,4)
        if c == 0:
            y1.append(-100*i)
        elif c == 1:
            y2.append(-100*i)
        elif c == 2:
            y3.append(-100*i)
        elif c == 3:
            y4.append(-100*i)
        elif c == 4:
            y5.append(-100*i)
    return y1, y2, y3, y4, y5
    
def musica(modo):
    if modo == 0:
        return musica1()
    else:
        return musicaale()