# Es un anagrama? #


def es_anagrama(palabra1: str, palabra2: str) -> bool:
    # Convertimos a minúsculas y quitamos espacios
    palabra1 = palabra1.lower().strip()
    palabra2 = palabra2.lower().strip()

    # Verificamos que no estén vacías y que sean diferentes
    if not palabra1 or not palabra2 or palabra1 == palabra2:
        return False

    # Un anagrama debe tener la misma cantidad de letras
    if len(palabra1) != len(palabra2):
        return False

    # Ordenamos las letras y comparamos
    return sorted(palabra1) == sorted(palabra2)


# Entrada de datos
str1 = input("Escribe la primera palabra: ")
str2 = input("Escribe la segunda palabra: ")

# Verificación
if es_anagrama(str1, str2):
    print("¡Es un anagrama!")
else:
    print("No es un anagrama")
