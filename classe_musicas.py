import pygame
import random

def erro():
    sound = pygame.mixer.Sound("erro.ogg")
    sound.set_volume(2.0)
    sound.play(loops = 0)
            
def musica1():
    pygame.mixer.music.load('baile.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.2)
    
    oimusica = open('baile.txt', 'r')
    musicatxt = oimusica.readlines()
    oimusica.close()
    musicastr = list(musicatxt[0])
    musica = []
    for i in range (len(musicastr)):
        musica.append(int(musicastr[i]))
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    for i in range (len(musica)):
        if musica[i] == 0:
            y1.append(-100*i)
        elif musica[i] == 1:
            y2.append(-100*i)
        elif musica[i] == 2:
            y3.append(-100*i)
        elif musica[i] == 3:
            y4.append(-100*i)
        elif musica[i] == 4:
            y5.append(-100*i)
        elif musica[i] == 5:
            y1.append(-100*i)
            y3.append(-100*i)
        elif musica[i] == 6:
            y2.append(-100*i)
            y4.append(-100*i)
        elif musica[i] == 7:
            y4.append(-100*i)
            y3.append(-100*i)
            y5.append(-100*i)
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)
    return y1, y2, y3, y4, y5
    
    
def musica2():
    pygame.mixer.music.load('cliffs.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(1)

    oimusica = open('cliffs_of_dover.txt', 'r')
    musicatxt = oimusica.readlines()
    oimusica.close()
    musicastr = list(musicatxt[0])
    musica = []
    for i in range (len(musicastr)):
        musica.append(int(musicastr[i]))
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    for i in range (len(musica)):
        if musica[i] == 0:
            y1.append(-100*i)
        elif musica[i] == 1:
            y2.append(-100*i)
        elif musica[i] == 2:
            y3.append(-100*i)
        elif musica[i] == 3:
            y4.append(-100*i)
        elif musica[i] == 4:
            y5.append(-100*i)
        elif musica[i] == 5:
            y1.append(-100*i)
            y3.append(-100*i)
        elif musica[i] == 6:
            y2.append(-100*i)
            y4.append(-100*i)
        elif musica[i] == 7:
            y4.append(-100*i)
            y3.append(-100*i)
            y5.append(-100*i)
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)
            
    return y1, y2, y3, y4, y5
    
    
def musica3():
    pygame.mixer.music.load('House.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(1)

    oimusica = open('house_of_gold.txt', 'r')
    musicatxt = oimusica.readlines()
    oimusica.close()
    musicastr = list(musicatxt[0])
    musica = []
    for i in range (len(musicastr)):
        musica.append(int(musicastr[i]))
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    for i in range (len(musica)):
        if musica[i] == 0:
            y1.append(-100*i)
        elif musica[i] == 1:
            y2.append(-100*i)
        elif musica[i] == 2:
            y3.append(-100*i)
        elif musica[i] == 3:
            y4.append(-100*i)
        elif musica[i] == 4:
            y5.append(-100*i)
        elif musica[i] == 5:
            y1.append(-100*i)
            y3.append(-100*i)
        elif musica[i] == 6:
            y2.append(-100*i)
            y4.append(-100*i)
        elif musica[i] == 7:
            y4.append(-100*i)
            y3.append(-100*i)
            y5.append(-100*i)
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)
    
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
        return musicaale()
    elif modo == 1:
        return musica1()
    elif modo == 2:
        return musica2()
    elif modo == 3:
        return musica3()