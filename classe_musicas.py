class musicas:
    def musica_1():
        oimusica1 = open('doremifa.txt', 'r')
        musica1txt = oimusica1.readlines()
        oimusica1.close()
        musica1 = list(musica1txt[0])
        return musica1
        
        
print (musicas.musica_1())