import pygame

largura_tela = 800
altura_tela = 500

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Botões")

# imagens dos botoes
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

# classe dos botoes
class Botoes():
    def __init__(self, x, y, image): 
        # apenas coordenadas para saber onde vai o botao e sua imagem
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def desenhar_botao(self):
        # desenha botao na tela
        tela.blit(self.image, (self.rect.x, self.rect.y)) # criação dos retang


run = True
while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    pygame.display.update()

pygame.quit()