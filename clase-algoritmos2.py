import math


def Calcular_area(figura, *args):
    if figura == "circulo":
        radio = args[0]
        return math.pi * radio**2
    elif figura == "rectangulo":
        base, altura = args
        return base * altura
    elif figura == "cuadrado":
        lado = args[0]
        return lado**2
    elif figura == "triangulo":
        base, altura = args
        return (base * altura) / 2
    else:
        return "Figura no valida"


if __name__ == "__main__":
    tipo_figura = input(
        "Ingrese el tipo de figura (circulo,cuadrado , rectangulo, triangulo): "
    ).lower()
    if tipo_figura == "circulo":
        radio = float(input("Ingrese el radio del circulo: "))
        area = Calcular_area(tipo_figura, radio)
    elif tipo_figura == "rectangulo":
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        area = Calcular_area(tipo_figura, base, altura)
    elif tipo_figura == "cuadrado":
        lado = float(input("Ingrese el lado un del cuadrado"))
        area = Calcular_area(tipo_figura, lado)
    elif tipo_figura == "triangulo":
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = Calcular_area(tipo_figura, base, altura)
    else:
        area = "Figura no valida"

    print(f"El area del {tipo_figura} es: {area}")
