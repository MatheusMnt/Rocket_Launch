import pygame
import random

class LixoEspacial(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # Lista de nomes de arquivos de imagem disponíveis para o lixo espacial
        trash_images = ["sprites/Trash/Trash1.png", "sprites/Trash/Trash2.png", "sprites/Trash/Trash3.png"]

        self.image = pygame.image.load(random.choice(trash_images))
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, [width//2, height//2])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 5) * 120 # Posição inicial aleatória dentro das faixas permitidas
        self.rect.y = -100  # Começa no topo da tela

    def move_down(self, speed, time_elapsed):
        self.rect.y += (speed + time_elapsed/360)
