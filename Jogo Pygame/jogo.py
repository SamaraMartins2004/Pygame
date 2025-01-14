import pygame
from pygame.locals import *
from sys import exit
from random import randint

#inicialização
pygame.init()
pygame.mixer.init()

#Sons
musica = pygame.mixer.music.load('Sons do Jogo/musicaFundo.mp3')
pygame.mixer.music.set_volume(0.1) #abaixando o som da musica de fundo
pygame.mixer.music.play(-1) #o -1 serve para a musica ficar repetindo (em loop)
som = pygame.mixer.Sound('Sons do Jogo/somColisao.wav') #som da colisão
som.set_volume(1.00)

# Janela
largura = 640
altura = 480
tamanho_cobra =     A

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

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
    tela.fill((255, 255, 255))  # Cor branca no fundo

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            exit()

        #fazendo com que o retangulo se mova quando estiver pressionando a tecla
            
        teclas = pygame.key.get_pressed()

        if teclas[K_a]:
            x_cobra -= 20

        if teclas[K_d]:
            x_cobra += 20

        if teclas[K_w]:
            y_cobra -= 20

        if teclas[K_s]:
            y_cobra += 20

        #evitando que a cobra saia da janela
        
        if x_cobra < 0:
            x_cobra = 0

        elif x_cobra > largura - 20:
            x_cobra = largura - 20

        if y_cobra < 0:
            y_cobra = 0

        elif y_cobra > altura -20:
            y_cobra = altura -20

        # Desenhar a cobra
        cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))  

        #Desenhando a maça
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