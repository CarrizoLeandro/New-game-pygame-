import pygame, sys
from pygame.locals import *
#Variable Globales
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

    def movimientoDerecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()

    def movimientoIzquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento()

    def __movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left=0
            elif self.rect.right > 870:
                self.rect.right= 840
        

    def disparar(self,x,y):
        miProyectil=proyectil(x,y)
        self.listaDisparo.append(miProyectil)
    def dibujar (self, superficie):
        superficie.blit(self.ImagenNave,self.rect)

class proyectil (pygame.sprite.Sprite):
    def __init__(self, posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil = pygame.image.load("img/disparoa.jpg")
        self.rect = self.imageProyectil.get_rect()

        self.velocidadDisparo = 3

        self.rect.top=posy
        self.rect.left=posx
    def trayectoria(self):
        self.rect.top=self.rect.top - self.velocidadDisparo
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)

class Invasor (pygame.sprite.Sprite):
    def __init__(self, posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.imagenA = pygame.image.load("img/MarcianoA.jpg")
        self.imagenB = pygame.image.load("img/MarcianoB.jpg")

        self.listaImagenes=[self.imagenA,self.imagenB]
        self.posImagen = 0

        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()

        self.listaDisparo=[]
        self.velocidadDisparo = 20
        self.rect.top=posy
        self.rect.left=posx

        self.tiempoCambio =0


        
    def trayectoria(self):
        self.rect.top=self.rect.top - self.velocidadDisparo
    def dibujar(self,superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor,self.rect)
    def comportamiento (self,tiempo):
        if self.tiempoCambio == tiempo:
            self.posImagen +=1
            self.tiempoCambio+=1
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen=0
            

#Inicio de ventana
def SpaceInvader(): 
    pygame.init()
    venta=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    jugador= naveEspacial()

    DemoProyectil= proyectil(ancho/2, alto-30)
    enemigo=Invasor(100,100)
    enJuego= True
    reloj=pygame.time.Clock()

    while True:
        #Eventos
        venta.fill((0,0,0))
        reloj.tick(60)
        tiempo=pygame.time.get_ticks()//1000
        for evento in pygame.event.get():
            if evento.type == QUIT :
                pygame.quit()
                sys.exit()
            if enJuego==True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.movimientoIzquierda()
                    elif evento.key == K_RIGHT:
                        jugador.movimientoDerecha()
                    elif evento.key == K_SPACE:
                        x,y=jugador.rect.center
                        jugador.disparar((x-5),(y-50))
        jugador.dibujar(venta)
        enemigo.dibujar(venta)
        enemigo.comportamiento(tiempo)
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(venta)
                x.trayectoria()
                if x.rect.top <0:
                    jugador.listaDisparo.remove(x)
        pygame.display.update()

SpaceInvader()
