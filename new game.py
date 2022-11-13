import pygame, sys
from pygame.locals import *
#Cariable Globales
ancho= 900
alto =480

class naveEspacial(pygame.sprite.Sprite):
    """Clase para las naves"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave= pygame.image.load("img/nave.jpg")

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx= ancho/2
        self.rect.centery=alto-30

        self.listaDisparo=[]
        self.Vida= True

        self.velocidad = 20

    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left=0
            elif self.rect.right > 870:
                self.rect.right= 840
        

    def disparar(self):
        print ("Disparo")
    def dibujar (self, superficie):
        superficie.blit(self.ImagenNave,self.rect)

class proyectil (pygame.sprite.Sprite):
    def __init__(self, posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil = pygame.image.load("img/disparoa.jpg")
        self.rect = self.imageProyectil.get_rect()

        self.velocidadDisparo = 0.1

        self.rect.top=posy
        self.rect.left=posx
    def trayectoria(self):
        self.rect.top=self.rect.top - self.velocidadDisparo
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)

#Inicio de ventana
def SpaceInvader(): 
    pygame.init()
    venta=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    jugador= naveEspacial()

    DemoProyectil= proyectil(ancho/2, alto-30)

    enJuego= True

    while True:
        #Eventos
        venta.fill((0,0,0))
        jugador.movimiento()
        DemoProyectil.trayectoria()
        for evento in pygame.event.get():
            if evento.type == QUIT :
                pygame.quit()
                sys.exit()
            if enJuego==True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.rect.left -= jugador.velocidad
                    elif evento.key == K_RIGHT:
                        jugador.rect.right += jugador.velocidad
                    elif evento.key == K_BACKSPACE:
                        jugador.disparar()
        DemoProyectil.dibujar(venta)
        jugador.dibujar(venta)
        pygame.display.update()

SpaceInvader()
