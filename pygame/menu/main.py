import pygame

pygame.init()

# tela
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Menu")

def desenha_texto(texto, fonte, texto_col, x, y):
    img = fonte.render(texto, True, texto_col)
    tela.blit(img, (x, y))

run = True
while run:

    tela.fill((52, 78, 91))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    pygame.display.update()

pygame.quit()
