# Números primos del 1 al 100 #


def es_primo(numero):
    # Si el número es menor o igual a 1, no es primo
    if numero <= 1:
        return False

    # Verificamos si es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True


def mostrar_primos():
    # Recorremos los números del 1 al 100
    for numero in range(1, 101):
        if es_primo(numero):
            print(f"{numero} es un número primo")
        else:
            print(f"{numero} no es un número primo")


if __name__ == "__main__":
    mostrar_primos()
