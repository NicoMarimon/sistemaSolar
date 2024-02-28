import math, pygame, random

class Asteroid():
    def __init__(self, radio, rango, angulo, color, escala, radio_sol, velocidad):
        self.velocidad = velocidad
        self.escala = escala
        self.radio = radio / self.escala
        self.distancia = (random.randint(rango[0],rango[1]) + radio_sol + self.radio)  / escala
        self.angulo = angulo
        self.color = color

    def mostrar(self, screen, anchura_pantalla, altura_pantalla, escala):
        centro_x = int(anchura_pantalla/2)
        centro_y = int(altura_pantalla/2)

        x = round(self.distancia / escala * math.cos(self.angulo) + centro_x)
        y = round(self.distancia /escala * math.sin(self.angulo) + centro_y)

        pygame.draw.circle(screen, self.color, (x, y), self.radio / escala)
