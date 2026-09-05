import pygame

largura_tela = 800
altura_tela = 500

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Botões")

# imagens dos botoes
start_img = pygame.image.load('./pygame/button/start_btn.png').convert_alpha()
exit_img = pygame.image.load('./pygame/button/exit_btn.png').convert_alpha()

# classe dos botoes
class Botao():
    def __init__(self, x, y, image, escala): 
        # apenas coordenadas para saber onde vai o botao e sua imagem
        largura_img = image.get_width()
        altura_img = image.get_height()
        self.image = pygame.transform.scale(image, (int(largura_img*escala), int(altura_img*escala)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def desenhar_botao(self):
        # pegar posição do mouse
        pos = pygame.mouse.get_pos()

        # checando mouse hover e clique
        if (self.rect.collidepoint(pos)):
            print('HOVER')

        # desenha botao na tela
        tela.blit(self.image, (self.rect.x, self.rect.y)) # criação dos retang


# instancias de botoes
start_button = Botao(100, 200, start_img, 0.8)
exit_button = Botao(450, 200, exit_img, 0.8)

run = True
while run:

    # desenhar botoes
    tela.fill((202, 228, 241))
    start_button.desenhar_botao()
    exit_button.desenhar_botao()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    pygame.display.update()

pygame.quit()