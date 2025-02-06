#crear un menu que sirva como interfaz para la calculadora de areas y perimetros que se vincule con el archivo de fucniones.py
import sys
from funciones import *

def mostrar_menu():
    print("Selecciona una figura:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Triángulo")
    print("5. Pentágono")
    print("6. Hexágono")
    print("7. Salir")

def obtener_opcion():
    try:
        opcion = int(input("Elige una opción (1-7): "))
        return opcion
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return None

def obtener_datos_figura(opcion):
    if opcion == 1:  # Círculo
        radio = float(input("Ingresa el radio del círculo: "))
        return radio,
    elif opcion == 2:  # Cuadrado
        lado = float(input("Ingresa el lado del cuadrado: "))
        return lado,
    elif opcion == 3:  # Rectángulo
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        return base, altura
    elif opcion == 4:  # Triángulo
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        lado1 = float(input("Ingresa el primer lado del triángulo: "))
        lado2 = float(input("Ingresa el segundo lado del triángulo: "))
        return base, altura, lado1, lado2
    elif opcion == 5:  # Pentágono
        lado = float(input("Ingresa el lado del pentágono: "))
        apotema = float(input("Ingresa el apotema del pentágono: "))
        return lado, apotema
    elif opcion == 6:  # Hexágono
        lado = float(input("Ingresa el lado del hexágono: "))
        apotema = float(input("Ingresa el apotema del hexágono: "))
        return lado, apotema
    else:
        print("Opción no válida.")
        return None

def mostrar_resultados(figura, datos, tipo_calculo):
    if figura == "Círculo":
        area, perimetro = circulo(*datos)
    elif figura == "Cuadrado":
        area, perimetro = cuadrado(*datos)
    elif figura == "Rectángulo":
        area, perimetro = rectangulo(*datos)
    elif figura == "Triángulo":
        area, perimetro = triangulo(*datos)
    elif figura == "Pentágono":
        area, perimetro = pentagono(*datos)
    elif figura == "Hexágono":
        area, perimetro = hexagono(*datos)
    
    if tipo_calculo == "Área":
        print(f"El área del {figura} es: {area}")
    elif tipo_calculo == "Perímetro":
        print(f"El perímetro del {figura} es: {perimetro}")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == 7:
            print("Saliendo...")
            sys.exit()
        
        if opcion not in range(1, 7):
            print("Opción inválida.")
            continue
        
        figura = ""
        if opcion == 1:
            figura = "Círculo"
        elif opcion == 2:
            figura = "Cuadrado"
        elif opcion == 3:
            figura = "Rectángulo"
        elif opcion == 4:
            figura = "Triángulo"
        elif opcion == 5:
            figura = "Pentágono"
        elif opcion == 6:
            figura = "Hexágono"
        
        datos = obtener_datos_figura(opcion)
        
        print("Selecciona el cálculo que deseas hacer:")
        print("1. Área")
        print("2. Perímetro")
        tipo_calculo = input("Elige una opción (1-2): ")
        
        if tipo_calculo == "1":
            mostrar_resultados(figura, datos, "Área")
        elif tipo_calculo == "2":
            mostrar_resultados(figura, datos, "Perímetro")
        else:
            print("Opción no válida.")
            continue

if __name__ == "__main__":
    ejecutar_calculadora()
