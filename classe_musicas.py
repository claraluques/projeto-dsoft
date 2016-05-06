class musicas:
    def musica_1():
        oimusica1 = open('doremifa.txt', 'r')
        musica1txt = oimusica1.readlines()
        oimusica1.close()
        musica1str = list(musica1txt[0])
        musica1 = []
        for i in range (len(musica1str)):
            musica1.append(int(musica1str[i]))
        return musica1
        
