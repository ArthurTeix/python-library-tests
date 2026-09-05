import pygame
from botao import tela, Botao

pygame.init()

# variaveis do jogo
jogo_pausado = False
menu_estado = 'main'

# definir fonte
fonte = pygame.font.SysFont("arialblack", 40) # difinição de fonte e tamanho

# definir cor
TEXTO_COR = (255, 255, 255)

# imagens
resume_img = pygame.image.load('./pygame/menu/img/button_resume.png').convert_alpha()
options_img = pygame.image.load('./pygame/menu/img/button_options.png').convert_alpha()
quit_img = pygame.image.load('./pygame/menu/img/button_quit.png').convert_alpha()
video_img = pygame.image.load('./pygame/menu/img/button_video.png').convert_alpha()
audio_img = pygame.image.load('./pygame/menu/img/button_audio.png').convert_alpha()
keys_img = pygame.image.load('./pygame/menu/img/button_keys.png').convert_alpha()
back_img = pygame.image.load('./pygame/menu/img/button_back.png').convert_alpha()

# instancias dos botoes
resume_botao = Botao(304, 125, resume_img, 1)
options_botao = Botao(297, 250, options_img, 1)
quit_botao = Botao(336, 375, quit_img, 1)
video_botao = Botao(226, 75, video_img, 1)
audio_botao = Botao(225, 200, audio_img, 1)
keys_botao = Botao(246, 325, keys_img, 1)
back_botao = Botao(332, 450, back_img, 1)

def desenha_texto(texto, fonte, texto_cor, x, y):
    img = fonte.render(texto, True, texto_cor)
    tela.blit(img, (x, y))

run = True
while run:

    tela.fill((52, 78, 91)) # cor de fundo

    # checando se jogo ta pausado
    if jogo_pausado:
        # checando estado do menu
        if (menu_estado == "main"):
            # botoes da tela de pausa
            if resume_botao.desenhar_botao():
                jogo_pausado = False
            if options_botao.desenhar_botao():
                menu_estado = 'options'
            if quit_botao.desenhar_botao():
                run = False

        # checagem se o menu de opcoes ta aberto
        if (menu_estado == 'options'):
            # desenhe as opções
            if video_botao.desenhar_botao():
                print("Configuracoes de Video")
            if audio_botao.desenhar_botao():
                print("Configuracoes de Audio")
            if keys_botao.desenhar_botao():
                print("Configuracoes de Keys")
            if back_botao.desenhar_botao():
                menu_estado = 'main'

    else:
        desenha_texto("Aperte Espaço Para Pausar", fonte, TEXTO_COR, 90, 250)

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                jogo_pausado = True

        if (event.type == pygame.QUIT):
            run = False

    pygame.display.update()

pygame.quit()
