import pygame
from classBtn import tela, start_button, exit_button

pygame.display.set_caption("Botões")

run = True
while run:

    # desenhar botoes
    tela.fill((202, 228, 241))

    if start_button.desenhar_botao():
        print('START')

    if exit_button.desenhar_botao():
        run = False

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    pygame.display.update()

pygame.quit()
