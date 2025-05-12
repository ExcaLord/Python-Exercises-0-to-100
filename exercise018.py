# Fibonacci Sequence
# La secuencia de Fibonacci es una serie donde cada número es la suma de los dos anteriores
# Por ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# Iniciamos con los dos primeros números de la secuencia
list_fibonacci = [0, 1]

# Pedimos al usuario cuántos números quiere ver
n = int(input("¿Cuántos números de la secuencia Fibonacci quieres ver? "))

# Generamos la secuencia
print(f"\nGenerando secuencia Fibonacci de {n} números:")
print(f"Comenzamos con: {list_fibonacci}")

for i in range(2, n):
    # Tomamos los dos últimos números
    ultimo = list_fibonacci[-1]
    penultimo = list_fibonacci[-2]

    # Calculamos el siguiente número
    next_num = ultimo + penultimo
    list_fibonacci.append(next_num)

    # Mostramos el proceso
    print(f"Número {i + 1}: {penultimo} + {ultimo} = {next_num}")

print(f"\nSecuencia Fibonacci completa: {list_fibonacci}")
