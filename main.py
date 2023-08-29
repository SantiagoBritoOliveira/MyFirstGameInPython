import pygame

import random

pygame.init()


largura_X = 400
Altura_Y = 400
frames = 60
rodando = True

tela = pygame.display.set_mode((largura_X, Altura_Y))
relogio = pygame.time.Clock()

class personagem:
    def __init__(self, x, y, vel, scale):
        self.posx = x
        self.posy = y
        self.altura = 20 * scale / 8
        self.largura = 20 * scale / 8
        self.velocidade = vel / random.randint(1, 10)
        self.cor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


    def addPosX(self):
        if(self.posx >= 400):
            self.posx = 0 - self.largura
        self.posx += 1 * self.velocidade

    def addPosY(self):
        self.posy += 1 * self.velocidade

    def decrementPosX(self):
        self.posx -= 1 * self.velocidade

    def decrementPosY(self):
        self.posy -= 1 * self.velocidade
        

    def exibirTela(self):
        pygame.draw.circle(tela, self.cor, (self.posx, self.posy), self.largura)

n_maximo = 100
listaDePlayers = []
for i in range(n_maximo):
    listaDePlayers.append(personagem(random.randint(0, 400),random.randint(0, 400), random.randint(1, 5), random.randint(0, 10)))


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    tela.fill("black")
    for i in range(n_maximo):
        listaDePlayers[i].exibirTela()

        if(teclas[pygame.K_w]):
            listaDePlayers[i].decrementPosY()
        elif(teclas[pygame.K_s]):
            listaDePlayers[i].addPosY()
        elif(teclas[pygame.K_a]):
            listaDePlayers[i].decrementPosX()
        elif(teclas[pygame.K_d]):
            listaDePlayers[i].addPosX()

        listaDePlayers[i].addPosX()

    pygame.display.flip()

    relogio.tick(frames)
