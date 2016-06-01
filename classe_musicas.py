import pygame
import random
    
#função do som de erro
    
def erro():
    sound = pygame.mixer.Sound("erro.ogg")
    sound.set_volume(2.0)
    sound.play(loops = 0)
       
#funções que leem a lista de notas e transforma em listaas de posições para cada botão
       #uma para cada musica
def musica1():
    pygame.mixer.music.load('comws.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.2)
    
    oimusica = open('comws.txt', 'r')
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
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)

    return y1, y2, y3, y4, y5, len(musica)
    
    
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
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)
    
    return y1, y2, y3, y4, y5, len(musica)
    
    
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
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)
    
    return y1, y2, y3, y4, y5, len(musica)
            
def musica4():
    pygame.mixer.music.load('ritd.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.7)

    oimusica = open('ritd.txt', 'r')
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
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)

    return y1, y2, y3, y4, y5, len(musica)
            
def musica5():
    pygame.mixer.music.load('fio.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(1)

    oimusica = open('fio.txt', 'r')
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
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)
    return y1, y2, y3, y4, y5, len(musica)

def musica6():
    pygame.mixer.music.load('br.mp3')
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(1)

    oimusica = open('br.txt', 'r')
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
        elif musica[i] == 9:
            y1.append(-100*i)
            y2.append(-100*i)
    return y1, y2, y3, y4, y5, len(musica)
    
#def musica7():
#    pygame.mixer.music.load('.mp3')
#    pygame.mixer.music.play(0)
#    pygame.mixer.music.set_volume(1)
#
#    oimusica = open('.txt', 'r')
#    musicatxt = oimusica.readlines()
#    oimusica.close()
#    musicastr = list(musicatxt[0])
#    musica = []
#    for i in range (len(musicastr)):
#        musica.append(int(musicastr[i]))
#    y1=[]
#    y2=[]
#    y3=[]
#    y4=[]
#    y5=[]
#    for i in range (len(musica)):
#        if musica[i] == 0:
#            y1.append(-100*i)
#        elif musica[i] == 1:
#            y2.append(-100*i)
#        elif musica[i] == 2:
#            y3.append(-100*i)
#        elif musica[i] == 3:
#            y4.append(-100*i)
#        elif musica[i] == 4:
#            y5.append(-100*i)
#        elif musica[i] == 5:
#            y1.append(-100*i)
#            y3.append(-100*i)
#        elif musica[i] == 6:
#            y2.append(-100*i)
#            y4.append(-100*i)
#        elif musica[i] == 9:
#            y1.append(-100*i)
#            y2.append(-100*i)
#    return y1, y2, y3, y4, y5, len(musica)

#def musica8():
#    pygame.mixer.music.load('.mp3')
#    pygame.mixer.music.play(0)
#    pygame.mixer.music.set_volume(1)
#
#    oimusica = open('.txt', 'r')
#    musicatxt = oimusica.readlines()
#    oimusica.close()
#    musicastr = list(musicatxt[0])
#    musica = []
#    for i in range (len(musicastr)):
#        musica.append(int(musicastr[i]))
#    y1=[]
#    y2=[]
#    y3=[]
#    y4=[]
#    y5=[]
#    for i in range (len(musica)):
#        if musica[i] == 0:
#            y1.append(-100*i)
#        elif musica[i] == 1:
#            y2.append(-100*i)
#        elif musica[i] == 2:
#            y3.append(-100*i)
#        elif musica[i] == 3:
#            y4.append(-100*i)
#        elif musica[i] == 4:
#            y5.append(-100*i)
#        elif musica[i] == 5:
#            y1.append(-100*i)
#            y3.append(-100*i)
#        elif musica[i] == 6:
#            y2.append(-100*i)
#            y4.append(-100*i)
#        elif musica[i] == 9:
#            y1.append(-100*i)
#            y2.append(-100*i)
#    return y1, y2, y3, y4, y5, len(musica)

#def musica9():
#    pygame.mixer.music.load('.mp3')
#    pygame.mixer.music.play(0)
#    pygame.mixer.music.set_volume(1)
#
#    oimusica = open('.txt', 'r')
#    musicatxt = oimusica.readlines()
#    oimusica.close()
#    musicastr = list(musicatxt[0])
#    musica = []
#    for i in range (len(musicastr)):
#        musica.append(int(musicastr[i]))
#    y1=[]
#    y2=[]
#    y3=[]
#    y4=[]
#    y5=[]
#    for i in range (len(musica)):
#        if musica[i] == 0:
#            y1.append(-100*i)
#        elif musica[i] == 1:
#            y2.append(-100*i)
#        elif musica[i] == 2:
#            y3.append(-100*i)
#        elif musica[i] == 3:
#            y4.append(-100*i)
#        elif musica[i] == 4:
#            y5.append(-100*i)
#        elif musica[i] == 5:
#            y1.append(-100*i)
#            y3.append(-100*i)
#        elif musica[i] == 6:
#            y2.append(-100*i)
#            y4.append(-100*i)
#        elif musica[i] == 9:
#            y1.append(-100*i)
#            y2.append(-100*i)
#    return y1, y2, y3, y4, y5, len(musica)

#função da musica gerada aleatoriamente
def musicaale():
    nbolinhas = 5
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    for i in range (nbolinhas):
        c = random.randint(0,9)
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
        elif c == 5:
            y1.append(-100*i)
            y3.append(-100*i)
        elif c == 6:
            y2.append(-100*i)
            y4.append(-100*i)
        elif c == 9:
            y1.append(-100*i)
            y2.append(-100*i)
    
    return y1, y2, y3, y4, y5, len(musica)
    
    
#função que define qual musica será rodada ao escolher o modo através dos botoes no codigo principal
def musica(modo):
    if modo == 0:
        m = musicaale()
    elif modo == 1:
        m = musica1()
    elif modo == 2:
        m = musica2()
    elif modo == 3:
        m = musica3()
    elif modo == 4:
        m = musica4()
    elif modo == 5:
        m = musica5()
    elif modo == 6:
        m = musica6()
#    elif modo == 7:
#        m = musica7()
#    elif modo == 8:
#        m = musica8()
#    elif modo == 9:
#        m = musica9()
    else:
        m = -1
    return m