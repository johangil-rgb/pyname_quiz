# librerias
import pygame
import sys
import random
import math

# iniciar pygame
pygame.init()

# tamaño ventana
ancho=900
alto=600

# crear ventana
pantalla=pygame.display.set_mode((ancho,alto))

# titulo ventana
pygame.display.set_caption("Tren en movimiento")

# reloj fps
clock=pygame.time.Clock()

# colores
cielo=(135,206,235)
verde=(80,180,80)
negro=(0,0,0)
gris=(120,120,120)
gris_claro=(200,200,200)
gris_oscuro=(70,70,70)
rojo=(180,30,30)
marron=(120,70,20)
amarillo=(255,220,0)
blanco=(255,255,255)

# movimiento fondo
x_fondo=0

# humo
humo=[]

# giro ruedas
angulo=0

# vibracion tren
movimiento=0

# fuente texto
fuente=pygame.font.SysFont("Times New Roman",40)

# ciclo principal
while True:

    # cerrar ventana
    for evento in pygame.event.get():

        if evento.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    # cielo
    pantalla.fill(cielo)

    # sol
    pygame.draw.circle(pantalla,amarillo,(760,90),50)

    # montaña 1
    pygame.draw.polygon(pantalla,gris,[(x_fondo+0,300),(x_fondo+150,150),(x_fondo+300,300)])

    # montaña 2
    pygame.draw.polygon(pantalla,gris,[(x_fondo+250,300),(x_fondo+450,120),(x_fondo+650,300)])

    # montaña 3
    pygame.draw.polygon(pantalla,gris,[(x_fondo+500,300),(x_fondo+700,170),(x_fondo+900,300)])

    # montaña 4
    pygame.draw.polygon(pantalla,gris,[(x_fondo+900,300),(x_fondo+1050,150),(x_fondo+1200,300)])

    # pasto
    pygame.draw.rect(pantalla,verde,(0,300,900,300))

    # riel arriba
    pygame.draw.rect(pantalla,negro,(0,450,900,8))

    # riel abajo
    pygame.draw.rect(pantalla,negro,(0,500,900,8))

    # madera vias
    for i in range(-40,1000,40):

        pygame.draw.rect(pantalla,marron,(i+(x_fondo%40),445,20,65))

    # vibracion tren
    movimiento=math.sin(pygame.time.get_ticks()*0.02)*3

    # frente tren hacia adelante
    pygame.draw.rect(pantalla,gris,(300,300+movimiento,70,90))

    # circulo frente
    pygame.draw.circle(pantalla,gris_oscuro,(370,345+int(movimiento)),35)

    # cuerpo tren
    pygame.draw.rect(pantalla,gris_claro,(120,240+movimiento,230,150))

    # cabina
    pygame.draw.rect(pantalla,gris,(120,120+movimiento,120,120))

    # techo cabina
    pygame.draw.rect(pantalla,gris_oscuro,(100,90+movimiento,160,35))

    # chimenea
    pygame.draw.rect(pantalla,gris,(300,170+movimiento,50,90))

    # techo chimenea
    pygame.draw.rect(pantalla,gris_oscuro,(290,150+movimiento,70,20))

    # cara
    pygame.draw.circle(pantalla,amarillo,(180,180+int(movimiento)),40)

    # ojo izquierdo
    pygame.draw.circle(pantalla,blanco,(165,165+int(movimiento)),10)

    # ojo derecho
    pygame.draw.circle(pantalla,blanco,(195,165+int(movimiento)),10)

    # pupila izquierda
    pygame.draw.circle(pantalla,marron,(165,165+int(movimiento)),5)

    # pupila derecha
    pygame.draw.circle(pantalla,marron,(195,165+int(movimiento)),5)

    # ceja izquierda
    pygame.draw.line(pantalla,amarillo,(155,145+movimiento),(170,155+movimiento),4)

    # ceja derecha
    pygame.draw.line(pantalla,amarillo,(205,145+movimiento),(190,155+movimiento),4)

    # boca
    pygame.draw.circle(pantalla,rojo,(180,200+int(movimiento)),10)

    # texto nombre
    texto=fuente.render("Johan",True,negro)

    # mostrar texto
    pantalla.blit(texto,(170,300+movimiento))

    # ruedas
    ruedas=[(140,410),(240,410),(340,410)]

    for rueda in ruedas:

        # posicion rueda
        x=rueda[0]
        y=rueda[1]+movimiento

        # rueda
        pygame.draw.circle(pantalla,gris,(x,y),45)

        # centro rueda
        pygame.draw.circle(pantalla,gris_oscuro,(x,y),10)

        # lineas ruedas
        x2=x+math.cos(angulo)*35
        y2=y+math.sin(angulo)*35

        x3=x-math.cos(angulo)*35
        y3=y-math.sin(angulo)*35

        # linea girando
        pygame.draw.line(pantalla,negro,(x2,y2),(x3,y3),4)

    # barra ruedas izquierda
    pygame.draw.rect(pantalla,negro,(140,398+movimiento,70,20))

    # barra ruedas derecha
    pygame.draw.rect(pantalla,negro,(240,398+movimiento,70,20))

    # crear humo
    if random.randint(1,10)==1:

        humo.append([320,150+movimiento,random.randint(8,18)])

    # mover humo
    for h in humo:

        h[1]-=2
        h[0]+=random.randint(-1,1)

        # dibujar humo
        pygame.draw.circle(pantalla,gris_claro,(int(h[0]),int(h[1])),h[2])

    # borrar humo viejo
    humo=[h for h in humo if h[1]>0]

    # mover fondo
    x_fondo-=4

    # reiniciar fondo
    if x_fondo<=-900:
        x_fondo=0

    # girar ruedas
    angulo+=0.2

    # actualizar pantalla
    pygame.display.update()

    # fps
    clock.tick(60)