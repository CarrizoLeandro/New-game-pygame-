import pygame, sys
from pygame.locals import *
#Inicio de ventana
pygame.init()
ventana = pygame.display.set_mode((800,700))
pygame.display.set_caption("Hola mundo")
#Fondo=(225,22
Cannon_img= pygame.image.load("img/cannon.webp")

#Se agrega Cañon
New_Cannon_img=pygame.transform.scale(Cannon_img,(int(100),int(100)))
posX,posY=350,610

#Velocidad
velocidad=15
#

while True:
    ventana.fill((225,225,225))
    ventana.blit(New_Cannon_img,(posX,posY))
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==K_LEFT:
                posX-=velocidad
            elif event.key==K_RIGHT:
                posX+=velocidad







    pygame.display.update()
