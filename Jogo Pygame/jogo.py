import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicialização
pygame.init()
pygame.mixer.init()

# Sons 
pygame.mixer.music.load('./Jogo Pygame/Sons do Jogo/musicaFundo.mp3')
pygame.mixer.music.set_volume(0.1)  # Abaixando o som da música de fundo
pygame.mixer.music.play(-1)  # Música em loop
som = pygame.mixer.Sound('./Jogo Pygame/Sons do Jogo/somColisao.wav')  # Som da colisão
som.set_volume(1.0)

# Configurações da janela
largura = 640
altura = 480
tamanho_cobra = 20

x_cobra = largura // 2
y_cobra = altura // 2

velocidade = 20
x_controle = velocidade
y_controle = 0

# Coordenadas da maçã
x_maca = randint(40, 600)
y_maca = randint(50, 430)

# Fonte e contador de pontos
fonte = pygame.font.SysFont('arial', 30, bold=True, italic=True)
pontos = 0

# Configurando a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 5
morreu = False

#criando a função de aumentar o tamanho da cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1],tamanho_cobra,tamanho_cobra))

#função para reiniciar o jogo
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra,y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura // 2
    y_cobra = altura // 2
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

fps_inicial = 10  
velocidade_inicial = 20  

# Loop principal
while True:
    # Aumentar a velocidade com base no número de pontos
    if pontos % 5 == 0 and pontos > 0:  # A cada 5 pontos, aumenta a velocidade
        fps_inicial += 1  # Aumenta o FPS
        velocidade_inicial += 2  # Aumenta a velocidade da cobra
        pontos += 1  # Evita que o aumento de velocidade aconteça várias vezes em um único ponto

    relogio.tick(fps_inicial)  # FPS ajustado com base no número de pontos
    tela.fill((255, 255, 255))  # Fundo branco

    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimento da cobra
    teclas = pygame.key.get_pressed()
    if teclas[K_a] and x_controle != velocidade:  # Movimento para a esquerda
        x_controle = -velocidade
        y_controle = 0
    if teclas[K_d] and x_controle != -velocidade:  # Movimento para a direita
        x_controle = velocidade
        y_controle = 0
    if teclas[K_w] and y_controle != velocidade:  # Movimento para cima
        y_controle = -velocidade
        x_controle = 0
    if teclas[K_s] and y_controle != -velocidade:  # Movimento para baixo
        y_controle = velocidade
        x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

    # Limites da janela
    if x_cobra >= largura:
        x_cobra = 0
    elif x_cobra < 0:
        x_cobra = largura - tamanho_cobra
    if y_cobra >= altura:
        y_cobra = 0
    elif y_cobra < 0:
        y_cobra = altura - tamanho_cobra

    # Desenhar a cobra e a maçã
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, tamanho_cobra, tamanho_cobra))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, tamanho_cobra, tamanho_cobra))

      # Verificar colisão com a maçã
    if cobra.colliderect(maca):
        x_maca = randint(40, largura - 40)
        y_maca = randint(50, altura - 50)
        pontos += 1
        som.play()
        comprimento_inicial += 1

    # Aumentar o tamanho da cobra
    lista_cabeca = [x_cobra, y_cobra]
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    #Quando houver colisão com o próprio corpo
    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            fonte2 = pygame.font.SysFont('arial', 20, True, True)
            mensagem = "Game Over '3' Pressione a tecla R para reiniciar o jogo"
            texto_formatado = fonte2.render(mensagem, True, (255,0,0)) #texto sendo exibido em vermelho
            ret_texto = texto_formatado.get_rect(center=(largura // 2, altura // 2))
            tela.blit(texto_formatado, ret_texto)#duas barras para retornar o valor inteiro dessa divisão
            pygame.display.update() 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()  

                 #reiniciar o jogo clicando em R
                if event.type == KEYDOWN and event.key == K_r:
                    reiniciar_jogo()

    aumenta_cobra(lista_cobra)
            
    # Exibir pontos
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    tela.blit(texto_formatado, (450, 40))

    # Atualizar a tela
    pygame.display.update()