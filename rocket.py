from typing import Any
import pygame
from rocket_falling import Falling

NUM_SWITCH = 18
NUM_SWITCH_STATE_1 = 0
NUM_SWITCH_STATE_2 = 1
NUM_SWITCH_STATE_3 = 2

INITIAL_X = 370
INITIAL_Y = 180


class Rocket(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("sprites/Rocket/Rocket_FULL.png")
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, [width//2, height//2])
        #self.image = pygame.transform.scale(self.image, [50, 250])
        self.rect = pygame.Rect([INITIAL_X, INITIAL_Y, width//2, height//2])
        self.switchs = [True]*NUM_SWITCH
        self.state_foguete = 0
        self.status = True
        self.level = [0,0,0]


    def set_foguete(self):
        self.check_switch()
        width = 0
        height = 0

        if self.state_foguete == 1:
            self.image = pygame.image.load("sprites/Rocket/Rocket1.png")
            width, height = self.image.get_size()
        elif self.state_foguete == 2:
            self.image = pygame.image.load("sprites/Rocket/Rocket2.png")
            width, height = self.image.get_size()               
        elif self.state_foguete == 3:
           self.image = pygame.image.load("sprites/Rocket/Rocket3.png")
           width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, [width//2, height//2])
        self.rect.height = height//2
        self.rect.width = width // 2
        self.level = [self.state_foguete , self.rect.x, self.rect.y + height//2]
        #self.level = self.state_foguete
     
    
    def check_switch(self):

        primeira_ocorrencia_True = None
        #print(self.switchs)

        for i in range(len(self.switchs)):
            if self.switchs[i]:
                primeira_ocorrencia_True = i - 1
                break

        #print(primeira_ocorrencia_True)       
        if primeira_ocorrencia_True == NUM_SWITCH_STATE_1:
            self.state_foguete = 1          
        elif primeira_ocorrencia_True == NUM_SWITCH_STATE_2:
            self.state_foguete = 2         
        elif primeira_ocorrencia_True == NUM_SWITCH_STATE_3:
            self.state_foguete = 3          
        elif primeira_ocorrencia_True < 0 and self.state_foguete != 0:
            self.status = False
            gameOver = True
            
    def update(self, *args):

        keys = pygame.key.get_pressed() #Array de Bool 

        # Movimento
        if keys[pygame.K_a]:
           self.rect.x -= 5
        elif keys[pygame.K_d]:
           self.rect.x += 5

        # limites de Tela 
        if self.rect.x < 0:
            self.rect.x = 0
        elif (self.rect.x + self.rect.width) > 840:
            self.rect.x = 840 - self.rect.width

        # intera��o switch
        # somente para testes, na versao final deve usar o vetor vindo do driver
        if keys[pygame.K_1]:
            self.switchs[0] = False
        elif keys[pygame.K_2]:
            self.switchs[1] = False
        elif keys[pygame.K_3]:
            self.switchs[2] = False


        if keys[pygame.K_BACKSPACE]:
            print("OPA")
            self.set_foguete()
        
        
