import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800,700))
pygame.display.set_caption("Hola mundo")

Cannon_img= pygame.image.load("img/cannon.webp")
New_Cannon_img=pygame.transform.scale(Cannon_img,(int(100),int(100)))
posX,posY=350,610


ventana.blit(New_Cannon_img,(posX,posY))
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT :
            pygame.quit()
            sys.exit()
    pygame.display.update()
