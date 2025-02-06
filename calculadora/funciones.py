#calcular el area y perimetro del circulo, rectangulo, pentagono y hexagono al igual que el cuadrado usando la funcion math
import math

# Función para calcular el área y el perímetro del círculo
def circulo(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

# Función para calcular el área y el perímetro del cuadrado
def cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

# Función para calcular el área y el perímetro del rectángulo
def rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

# Función para calcular el área y el perímetro del triángulo
def triangulo(base, altura, lado1, lado2):
    area = (base * altura) / 2
    perimetro = base + lado1 + lado2
    return area, perimetro

# Función para calcular el área y el perímetro del pentágono
def pentagono(lado, apotema):
    area = (5 * lado * apotema) / 2
    perimetro = 5 * lado
    return area, perimetro

# Función para calcular el área y el perímetro del hexágono
def hexagono(lado, apotema):
    area = (6 * lado * apotema) / 2
    perimetro = 6 * lado
    return area, perimetro
