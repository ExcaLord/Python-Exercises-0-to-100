class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, edad, calificaciones):
        estudiante = {
            "nombre": nombre,
            "edad": edad,
            "calificaciones": calificaciones,
        }
        self.estudiantes.append(estudiante)
        print(f"Estudiante {nombre} agregado correctamente.")

    def calcular_promedio(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante["nombre"] == nombre:
                calificaciones = estudiante["calificaciones"]
                return sum(calificaciones) / len(calificaciones)
        return "Estudiante no encontrado."

    def listar_estudiantes(self):
        return [estudiante["nombre"] for estudiante in self.estudiantes]


# Uso del gestor de estudiantes

gestor = GestorEstudiantes()
print(gestor.agregar_estudiante("Ana", 20, [85, 90, 95]))
print(gestor.agregar_estudiante("Carlos", 22, [75, 80, 85]))
print(f"Promedio de Ana: {gestor.calcular_promedio('Carlos')}")
print(f"Lista de estudiantes: {gestor.listar_estudiantes()}")
