from typing import Any
import pygame
NUM_SWITCH = 10
NUM_SWITCH_STATE_1 = 0
NUM_SWITCH_STATE_2 = 1
NUM_SWITCH_STATE_3 = 2

INITIAL_X = 370
INITIAL_Y = 210

class Rocket(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("sprites/Rocket/Rocket_FULL.png")
        self.image = pygame.transform.scale(self.image, [50, 250])
        self.rect = pygame.Rect([INITIAL_X, INITIAL_Y, 50, 250])
        self.switchs = [True]*NUM_SWITCH
        self.state_foguete = 0
        self.status = True

    # def check_rocket_version(self, keys):
    #     if keys[pygame.K_SPACE] & self.switchs[1] and (not self.switchs[2]) and (not self.switchs[3]):
    #         self.state_foguete = 1
    #         self.set_foguete(self.state_foguete)
    #     elif keys[pygame.K_SPACE] & self.switchs[1] and (self.switchs[2]) and (not self.switchs[3]):
    #         self.state_foguete = 2
    #         self.set_foguete(self.state_foguete)
    #     elif keys[pygame.K_SPACE] & self.switchs[1] & self.switchs[2] & self.switchs[3]:
    #         self.state_foguete = 3
    #         self.set_foguete(self.state_foguete)

    def set_foguete(self):
        self.check_switch()      
        if self.state_foguete == 1:
            self.image = pygame.image.load("sprites/Rocket/Rocket1.png")          
        elif self.state_foguete == 2:
            self.image = pygame.image.load("sprites/Rocket/Rocket2.png")           
        elif self.state_foguete == 3:
           self.image = pygame.image.load("sprites/Rocket/Rocket3.png")
        self.image = pygame.transform.scale(self.image, [50, 250])
    
    def check_switch(self):

        primeira_ocorrencia_True = None
        print(self.switchs)

        for i in range(len(self.switchs)):
            if self.switchs[i]:
                primeira_ocorrencia_True = i - 1
                break

        print(primeira_ocorrencia_True)       
        if primeira_ocorrencia_True == NUM_SWITCH_STATE_1:
            self.state_foguete = 1           
        elif primeira_ocorrencia_True == NUM_SWITCH_STATE_2:
            self.state_foguete = 2         
        elif primeira_ocorrencia_True == NUM_SWITCH_STATE_3:
            self.state_foguete = 3          
        elif primeira_ocorrencia_True < 0 and self.state_foguete != 0:
            self.status = False
            print("Foguete Explodiu!")       
            
    def update(self, *args):

        keys = pygame.key.get_pressed() #Array de Bool 

        # Movimento
        if keys[pygame.K_a]:
           self.rect.x -= 5
        elif keys[pygame.K_d]:
           self.rect.x += 5
        elif keys[pygame.K_w] and self.state_foguete == 3:
           self.rect.y -= 5
        elif keys[pygame.K_s] and self.state_foguete == 3:
           self.rect.y += 5

        # limites de Tela 
        if self.rect.x < 0:
            self.rect.x = 0
        elif (self.rect.x + self.rect.width) > 840:
            self.rect.x = 840 - self.rect.width

        # interação switch
        # somente para testes, na versao final deve usar o vetor vindo do driver
        if keys[pygame.K_1]:
            self.switchs[0] = False
        elif keys[pygame.K_2]:
            self.switchs[1] = False
        elif keys[pygame.K_3]:
            self.switchs[2] = False

        if keys[pygame.K_BACKSPACE]:
            self.set_foguete()
        
        
