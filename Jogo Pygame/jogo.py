import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

musica_fundo = pygame.mixer.music.load('BoxCat Games - Trace Route.mp3')

#abaixando o som da musica de fundo
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) #o -1 serve para a musica ficar repetindo (em loop)

# Definindo o tamanho da janela no jogo
largura = 640
altura = 480

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

#som da colisão

som = pygame.mixer.Sound('smw_coin.wav')
som.set_volume(1.00)

#variaveis para que consiga gerar numeros aleatorios da posição do retangulo azul

x_maca = randint(40,600)
y_maca = randint(50,430)

#criando o contador dos pontos

fonte = pygame.font.SysFont('arial', 40, bold= True, italic=True) #definindo a fonte, tamanho, se estará em negrito e itálico

# Configurando a janela
tela = pygame.display.set_mode((largura, altura))

pontos = 0

# Definindo o nome que aparecerá na janela
pygame.display.set_caption("Meu Jogo")
relogio = pygame.time.Clock()

# Loop principal
while True:

    relogio.tick(50)
    tela.fill((255, 255, 255))  # Cor preta no fundo

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            exit()

        #fazendo com que o retangulo se mova quando estiver pressionando a tecla
        if pygame.key.get_pressed()[K_a]:
            x_cobra -= 20

        if pygame.key.get_pressed()[K_d]:
            x_cobra += 20

        if pygame.key.get_pressed()[K_w]:
            y_cobra -= 20

        if pygame.key.get_pressed()[K_s]:
            y_cobra += 20

        # Desenhar o retângulo vermelho
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))  

        #Desenhando o retangulo azul
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca,20,20))

    if cobra.colliderect(maca): # ver se houve colisão
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos += 1
        som.play()

        #Texto do contador de pontos
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))

    tela.blit(texto_formatado, (450,40))

    # Atualizar a tela
    pygame.display.update() 