import pygame
from rocket import Rocket

# print("Hello, World")

pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Teste Janela")

print(display.get_rect)

drawGroup = pygame.sprite.Group()
rocket = Rocket(drawGroup)

def draw():
    display.fill([25, 25, 112])

def contagem_regressiva():
    pygame.display.set_caption('Contagem Regressiva')

    fonte = pygame.font.SysFont(None, 100)

    for i in range(10, 0, -1):
    #display.fill((0, 0, 0))
        draw()
        texto = fonte.render(str(i), True, (255, 255, 255))
        texto_retangulo = texto.get_rect(center=(840 // 2, 480 // 2))
        display.blit(texto, texto_retangulo)
        pygame.display.flip()
        draw()
        pygame.time.wait(1000)  # Espera 1 segundo

gameloop = True
clock = pygame.time.Clock()
isPressingW = False
isPressingSpace = False
while gameloop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                isPressingSpace = True

    if isPressingSpace:
        contagem_regressiva()
        isPressingSpace = False
    else: 
        draw()
        drawGroup.update()
        drawGroup.draw(display)
        pygame.display.update()
    