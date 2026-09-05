import pygame

# tela
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Menu")

# classe dos botoes
class Botao():
    def __init__(self, x, y, image, escala): 
        # apenas coordenadas para saber onde vai o botao e sua imagem
        largura_img = image.get_width()
        altura_img = image.get_height()
        self.image = pygame.transform.scale(image, (int(largura_img*escala), int(altura_img*escala)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicado = False # controlador de cliques, para ser clicado apenas uma vez cada botão

    def desenhar_botao(self):
        # variável que vai definir as ações de cada botão
        action = False

        # pegar posição do mouse
        pos = pygame.mouse.get_pos()

        # checando mouse hover e clique
        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1) and (self.clicado == False):
                self.clicado = True
                action = True

        if (pygame.mouse.get_pressed()[0] == 0):
            self.clicado = False

        # desenha botao na tela
        tela.blit(self.image, (self.rect.x, self.rect.y)) # criação dos retang

        return action
