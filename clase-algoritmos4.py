tareas = []


def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")


def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Lista de tareas:")
        for indice, tarea in enumerate(tareas):
            print(f"{indice + 1}. {tarea}")


def eliminar_tarea(indice):
    try:
        indice = int(indice) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada}' eliminada")
        else:
            print("Indice no valido")
    except ValueError:
        print("Ingrese un valor valido")


if __name__ == "__main__":
    while True:
        print("\n--- Menu de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nueva_tarea = input("Ingrese la nueva tarea:")

