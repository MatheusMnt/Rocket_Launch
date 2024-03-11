import math
import pygame
import random
import sys

from rocket import Rocket
from background import Background

SIZE_WINDOW_X = 840
SIZE_WINDOW_Y = 480
FONTE_DEFAULT = "Fonts/GamegirlClassic.ttf"
BRANCO = (255, 255, 255)
MIDNIGHT_BLUE = (25, 25, 112)


pygame.init()

#seta configuracoes iniciais da janela 
display = pygame.display.set_mode([SIZE_WINDOW_X, SIZE_WINDOW_Y])
pygame.display.set_caption("Rocket Launch")

#crias classe de desenahveis da biblioteca
drawGroup = pygame.sprite.Group()

#cria foguete e adiciona ao grupo 
rocket = Rocket(drawGroup)


#Define Fontes 
title_font = pygame.font.Font(FONTE_DEFAULT, 50)
fonte = pygame.font.Font(FONTE_DEFAULT, 25)
fonte_combustivel = pygame.font.Font(FONTE_DEFAULT, 15)

def draw():
    display.fill(MIDNIGHT_BLUE)
   
# Funcao para desenhar um retangulo segmentado
def draw_segmented_rectangle(surface, color, x, y, width, height, segments, time_elapsed):
    segment_width = width // segments
    for i in range(segments):
        if i < (time_elapsed // 10):
            pygame.draw.rect(surface, MIDNIGHT_BLUE, (x + i * segment_width, y, segment_width, height), 0)
        else:
            pygame.draw.rect(surface, color, (x + i * segment_width, y, segment_width, height), 0)
        pygame.draw.rect(surface, BRANCO, (x + i * segment_width, y, segment_width, height), 1)  # Desenha linha de contorno

    # Desenha o texto "Combustivel" acima do retangulo
    texto_combustivel = fonte_combustivel.render("Combustivel", True, BRANCO)
    texto_combustivel_retangulo = texto_combustivel.get_rect(center=(x + width // 2, y - 25))
    surface.blit(texto_combustivel, texto_combustivel_retangulo)



#desenha relogio da contagem regressiva 
def draw_circle(angulo):
    draw()
    centro = (SIZE_WINDOW_X // 2, SIZE_WINDOW_Y // 2)
    raio = 50
    largura_linha = 3
    inicio_angulo = math.radians(0)
    fim_angulo = math.radians(angulo)
    pygame.draw.arc(display, BRANCO, (centro[0] - raio, centro[1] - raio, raio * 2, raio * 2), inicio_angulo, fim_angulo, largura_linha)

#desenha contagem Regressiva
def contagem_regressiva():
    for i in range(10, 0, -1):
        angulo = i * 36
        draw()
        draw_circle(angulo)
        texto = fonte.render(str(i), True, (255, 255, 255))
        texto_retangulo = texto.get_rect(center=(SIZE_WINDOW_X // 2, SIZE_WINDOW_Y // 2))
        display.blit(texto, texto_retangulo)
        pygame.display.flip()
        draw()
        pygame.time.wait(1000)  # Espera 1 segundo

#desenha o menu inicial 
def menu():
    draw()
    #desenha titulo do Jogo
    titulo = title_font.render("SpaCIN Ship ", True, (255, 255, 255))
    titulo_retangulo = titulo.get_rect(center=(SIZE_WINDOW_X // 2, 50))
    display.blit(titulo, titulo_retangulo)
    #desenha instrucao apra comecar o jogo 
    texto = fonte.render("Pressione SPACE para Lancar", True, (255, 255, 255))
    texto_retangulo = texto.get_rect(center=(SIZE_WINDOW_X // 2, SIZE_WINDOW_Y // 2))
    display.blit(texto, texto_retangulo)
    pygame.display.flip()
    draw()


#Clock para atualizacao de tela
clock = pygame.time.Clock()


#Flags de Controle
gameloop = True
gameStart = False
time_elapsed = 0

#loop principal do jogo 
while gameloop:

    clock.tick(60)
    #time_elapsed = pygame.time.get_ticks() / 1000  # Tempo decorrido em segundos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           gameloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gameStart:
                contagem_regressiva()
                gameStart = True
        elif not gameStart:
            menu()


    if gameStart:
        draw()
        drawGroup.update()
        drawGroup.draw(display)
        time_elapsed += 1 / 60 
        draw_segmented_rectangle(display, BRANCO, SIZE_WINDOW_X - 200, 50, 180, 50, 18, time_elapsed)
        pygame.display.update()
    