import pygame

largura_tela = 800
altura_tela = 500

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Botões")

run = True
while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    pygame.display.update()

pygame.quit()