import pygame, math


class Planet():
    def __init__(self, nombre, radio, distancia, angulo, color, escala, radio_sol):
        self.escala = escala
        self.nombre = nombre
        self.radio = radio / self.escala
        self.distancia = (distancia + radio_sol + self.radio)  / escala
        self.angulo = angulo
        self.color = color

    def mostrar(self, screen, anchura_pantalla, altura_pantalla, escala):
        centro_x = int(anchura_pantalla/2)
        centro_y = int(altura_pantalla/2)

        x = round(self.distancia / escala * math.cos(self.angulo) + centro_x)
        y = round(self.distancia /escala * math.sin(self.angulo) + centro_y)

        pygame.draw.circle(screen, self.color, (x, y), self.radio / escala)

