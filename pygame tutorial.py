import pygame

pygame.init()

display_width = 800
display_height = 600


black = (0,0,0)
white = (255,255,255)




gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(('Bolinha descendo!'))
clock = pygame.time.Clock()
crashed = False

bot1Img = pygame.image.load('botao1.png')
bot1Img = pygame.transform.scale(bot1Img, (50,100))


bot2Img = pygame.image.load('botao2.png')
bot2Img = pygame.transform.scale(bot2Img, (50,100))


def bot1(x, y):
    gameDisplay.blit(bot1Img,(x,y))

def bot2(x, y):
    gameDisplay.blit(bot2Img,( x+50 ,y-100))

x = (display_width/2)
y = (display_height*0.2)
y_change = 0


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                y_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
    
    
    
    y += y_change
    
    
    gameDisplay.fill(white)
    bot1(x, y)
    bot2(x, y)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()