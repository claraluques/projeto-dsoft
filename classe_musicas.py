class musicas:
    def musica1():
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