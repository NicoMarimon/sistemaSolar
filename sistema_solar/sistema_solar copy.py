import math, pygame, sys, random
from planet import Planet
# from spaceship import Nave

# IDEAS
#  1. Escala ajustable                                                                                   HECHO
#  2. Velocidad de los planetas ajustable                                                                HECHO
#  3. Nave que pueda ir moviendose por el espacio
#  4. Mientras nave se encuentre cerca o encima de un planeta que muestre los detalles del mismo
#  5. Navegador hacia el planeta que deseas ir segun el planeta que escojas
#  6. Satélites naturales, añadir las lunas de los planetas
#  7. Si está todo a escala 1 ajustar velocidad de la nave
#  8. Guardar partida con las coordenadas
#  9. Animar planetas, lunas, sol y nave 
# 10. Encontrar todos los planetas
# 11. Añadir Plutón
# 12. Optimizar crear planetas con bucle for
# 13. Rastro Planetas
# 14. Música relajante

# Inicializamos pygame
pygame.init()

# Configuración de la ventana
anchura_pantalla = pygame.display.Info().current_w
altura_pantalla = pygame.display.Info().current_h
pantalla = pygame.display.set_mode((anchura_pantalla, altura_pantalla))
pygame.display.set_caption('Sistema solar')

# Reloj para controlar la velocidad de los fotoframas
clock = pygame.time.Clock()
FPS = 60  # Velocidad de cuadros por segundo

# Colores
espacio_c = (0, 0, 0)

# Ajustes Generales
escala = 1
escala_tamaño_sol = 1



# FONDO
fondo = 'fondos/vialactea.jpg'  # Nombre del archivo de video
imagen_fondo = pygame.image.load(fondo).convert()

# NAVE
class Nave:
    def __init__(self, pos):
        self.original_image = pygame.image.load('imagenes/ship.png').convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else: 
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else: 
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed
        # Calcular el ángulo de rotación basado en la dirección
        angle = self.direction.angle_to(pygame.math.Vector2(0, -1))
        self.image = pygame.transform.rotate(self.original_image, angle)

nave = Nave((anchura_pantalla / 2, altura_pantalla/2))


# SOL
# Radio aprox = 696.340 km
Sol_r = 696.340
# Distancia al centro de la Vía Láctea aprox 27.000 años luz
# Duracion en rotar su eje aprox = 25-35 días terrestres
sol_c = (250, 180, 0)
radio_sol = 696.340 / escala_tamaño_sol



# PLANETAS

# LA TIERRA
Tierra_c = (0, 255, 255)

# Radio Tierra aprox = 6.371 km
Tierra_r = 6.371

# Distancia de la Tierra al Sol aprox = 149.000.000 km
Tierra_d = 149

# Duracion en dar la vuelta al Sol aprox = 365 días
Tierra_o = 365

# La velocidad de la Tierra será de 0.1 y servirá de base para definir el resto
def calcular_velocidad(orbita):
    velocidad = Tierra_o / orbita * Tierra_v
    return velocidad

Tierra_v = 0.1
Tierra = Planet('Tierra', Tierra_r, Tierra_d, random.randint(0, 360), Tierra_c, escala, radio_sol)




# MERCURIO
Mercurio_c = (200, 200, 200)

# Radio Mercurio aprox = 2,439 km
Mercurio_r = 2.439

# Distancia de Mercurio al Sol aprox = 58.000.000 km
Mercurio_d = 58

# Duracion en dar la vuelta al Sol aprox = 88 días
Mercurio_o = 88
# Velocidad Tierra = 0.1
#                        Duracion órbita Tierra
# Velocidad Mercurio = ------------------------- * Velocidad Tierra (0.1)
#                       Duracion órbita Mercurio
#                       365
# Velocidad Mercurio = ----- * 0.1 = 0.4 aprox
#                       88

Mercurio_v = calcular_velocidad(Mercurio_o)
Mercurio = Planet('Mercurio', Mercurio_r, Mercurio_d, random.randint(0, 360), Mercurio_c, escala, radio_sol)




# VENUS
Venus_c = (255, 160, 50)

# Radio Venus aprox = 6.052 km
Venus_r = 6.052

# Distancia de Venus al Sol aprox = 108.000.000 km
Venus_d = 108

# Duracion en dar la vuelta al Sol aprox = 255 días
Venus_o = 255
# Velocidad Tierra = 0.1
#                    Duracion órbita Tierra
# Velocidad Venus = ------------------------- * Velocidad Tierra (0.1)
#                     Duracion órbita Venus
#                    365
# Velocidad Venus = ----- * 0.1 = 1.4 aprox
#                    255
Venus_v = calcular_velocidad(Venus_o)
Venus = Planet('Venus', Venus_r, Venus_d, random.randint(0, 360), Venus_c, escala, radio_sol)




# MARTE
Marte_c = (255, 100, 50)

# Radio Marte aprox = 3.389 km
Marte_r = 3.389

# Distancia de Marte al Sol aprox = 228.000.000 km
Marte_d = 228

# Duracion en dar la vuelta al Sol aprox = 687 días
Marte_o = 687
# Velocidad Tierra = 0.1
#                    Duracion órbita Tierra
# Velocidad Marte = ------------------------- * Velocidad Tierra (0.1)
#                     Duracion órbita Marte
#                    365
# Velocidad Marte = ----- * 0.1 = 0.05 aprox
#                    687
Marte_v = calcular_velocidad(Marte_o)
Marte = Planet('Marte', Marte_r, Marte_d, random.randint(0, 360), Marte_c, escala, radio_sol)




# JÚPITER
Jupiter_c = (200, 100, 50)

# Radio Jupiter aprox = 69.911 km
Jupiter_r = 69.911

# Distancia de Jupiter al Sol aprox = 778.000.000 km
Jupiter_d = 778

# Duracion en dar la vuelta al Sol aprox = 4.333 días
Jupiter_o = 4333
# Velocidad Tierra = 0.1
#                      Duracion órbita Tierra
# Velocidad Jupiter = ------------------------- * Velocidad Tierra (0.1)
#                      Duracion órbita Jupiter
#                      365
# Velocidad Jupiter = ----- * 0.1 = 0.05 aprox
#                     4.333
Jupiter_v = calcular_velocidad(Jupiter_o)
Jupiter = Planet('Jupiter', Jupiter_r, Jupiter_d, random.randint(0, 360), Jupiter_c, escala, radio_sol)




# SATURNO
Saturno_c = (255, 215, 0)

# Radio Saturno aprox = 58.232 km
Saturno_r = 58.232

# Distancia de Saturno al Sol aprox = 1.429.000.000 km
Saturno_d = 1429

# Duracion en dar la vuelta al Sol aprox = 10.747 días
Saturno_o = 10747
# Velocidad Tierra = 0.1
#                      Duracion órbita Tierra
# Velocidad Saturno = ------------------------- * Velocidad Tierra (0.1)
#                      Duracion órbita Saturno
#                       365
# Velocidad Saturno = ------- * 0.1 = 0.003 aprox
#                      10.747
Saturno_v = calcular_velocidad(Saturno_o)
Saturno = Planet('Saturno', Saturno_r, Saturno_d, random.randint(0, 360), Saturno_c, escala, radio_sol)




# URANO
Urano_c = (0, 191, 255)

# Radio Urano aprox = 25.362 km
Urano_r = 25.362

# Distancia de Urano al Sol aprox = 2.871.000.000 km
Urano_d = 2871

# Duracion en dar la vuelta al Sol aprox = 30.589 días
Urano_o = 30589
# Velocidad Tierra = 0.1
#                      Duracion órbita Tierra
# Velocidad Urano = ------------------------- * Velocidad Tierra (0.1)
#                      Duracion órbita Urano
#                     365
# Velocidad Urano = ------- * 0.1 = 0.001 aprox
#                   30.589
Urano_v = calcular_velocidad(Urano_o)
Urano = Planet('Urano', 25.362, 2871, random.randint(0, 360), Urano_c, escala, radio_sol)




# NEPTUNO
Neptuno_c = (0, 0, 139)

# Radio Neptuno aprox = 24.622 km
Neptuno_r = 24.622

# Distancia de Neptuno al Sol aprox = 4.498.000.000 km
Neptuno_d = 4498

# Duracion en dar la vuelta al Sol aprox = 60.190 días
Neptuno_o = 60190
# Velocidad Tierra = 0.1
#                      Duracion órbita Tierra
# Velocidad Neptuno = ------------------------- * Velocidad Tierra (0.1)
#                      Duracion órbita Neptuno
#                       365
# Velocidad Neptuno = ------- * 0.1 = 0.0006 aprox
#                     60.190
Neptuno_v = calcular_velocidad(Neptuno_o)
Neptuno = Planet('Urano', Neptuno_r, Neptuno_d, random.randint(0, 360), Neptuno_c, escala, radio_sol)

lista_planetas = [Mercurio, Venus, Tierra, Marte, Jupiter, Saturno, Urano, Neptuno]


# Bucle principal
while True:
    # Control de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Ajustando escala
            if event.key == pygame.K_1:
                escala = 1
            if event.key == pygame.K_2:
                escala = 4
            if event.key == pygame.K_3:
                escala = 8
            if event.key == pygame.K_4:
                escala = 12

            # Ajustando velocidad
            if event.key == pygame.K_DOWN:
                if FPS == 30 or FPS == 60 or FPS == 45:
                    FPS -= 15
            if event.key == pygame.K_UP:
                if FPS == 15 or FPS == 30 or FPS == 45:
                    FPS += 15

        #     # Movimiento usuario
        #     if event.key == pygame.K_w:
        #         nave.movimiento[0] = True
        #     if event.key == pygame.K_d:
        #         nave.movimiento[1] = True
        #     if event.key == pygame.K_s:
        #         nave.movimiento[2] = True
        #     if event.key == pygame.K_a:
        #         nave.movimiento[3] = True

        # if event.type == pygame.KEYUP:
        #     # Movimiento usuario
        #     if event.key == pygame.K_w:
        #         nave.movimiento[0] = False
        #     if event.key == pygame.K_d:
        #         nave.movimiento[1] = False
        #     if event.key == pygame.K_s:
        #         nave.movimiento[2] = False
        #     if event.key == pygame.K_a:
        #         nave.movimiento[3] = False
        

    # Fondo
    pantalla.fill(espacio_c)
    # pantalla.blit(imagen_fondo, (0, 0))

    # SOL
    pygame.draw.circle(pantalla , sol_c, (anchura_pantalla/2, altura_pantalla/2), radio_sol / escala)

    for planeta in lista_planetas:
        planeta.escala = escala


    # PLANETAS
    Mercurio.angulo = Mercurio.angulo + Mercurio_v
    Mercurio.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)

    Venus.angulo = Venus.angulo + Venus_v
    Venus.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)

    Tierra.angulo = Tierra.angulo + Tierra_v
    Tierra.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)

    Marte.angulo = Marte.angulo + Marte_v
    Marte.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)

    Jupiter.angulo = Jupiter.angulo + Jupiter_v
    Jupiter.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)

    Saturno.angulo = Saturno.angulo + Saturno_v
    Saturno.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)
    
    Urano.angulo = Urano.angulo + Urano_v
    Urano.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)

    Neptuno.angulo = Neptuno.angulo + Neptuno_v
    Neptuno.mostrar(pantalla, anchura_pantalla, altura_pantalla, escala)
            
    # NAVE
    nave.update()
    pantalla.blit(nave.image, nave.rect.center)
            
    # Actualizar a pantalla
    pygame.display.flip()

    # Limitar la velocidad de FPS
    clock.tick(FPS)
