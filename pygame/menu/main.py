import pygame

pygame.init()

# tela
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Menu")

# definir fonte
fonte = pygame.font.SysFont("arialblack", 40) # difinição de fonte e tamanho

# definir cor
TEXTO_COR = (255, 255, 255)


def desenha_texto(texto, fonte, texto_cor, x, y):
    img = fonte.render(texto, True, texto_cor)
    tela.blit(img, (x, y))

run = True
while run:

    tela.fill((52, 78, 91)) # cor de fundo

    desenha_texto("Aperte Espaço Para Pausar", fonte, TEXTO_COR, 90, 250)

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                print('pause')

        if (event.type == pygame.QUIT):
            run = False

    pygame.display.update()

pygame.quit()
