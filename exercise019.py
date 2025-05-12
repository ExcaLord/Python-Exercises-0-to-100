class Human:
    def __init__(self, name: str, age: int, height: float, weight: float):
        """
        Inicializa un nuevo humano
        Args:
            name (str): Nombre del humano
            age (int): Edad en años
            height (float): Altura en metros
            weight (float): Peso en kilogramos
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.is_alive = True

    def calculate_bmi(self) -> float:
        """Calcula el índice de masa corporal (IMC)"""
        return self.weight / (self.height**2)

    def have_birthday(self):
        """Incrementa la edad del humano en un año"""
        self.age += 1
        print(f"¡Feliz cumpleaños {self.name}! Ahora tienes {self.age} años.")

    def introduce(self):
        """El humano se presenta"""
        bmi = self.calculate_bmi()
        return f"Hola, soy {self.name}. Tengo {self.age} años, mido {self.height}m y peso {self.weight}kg. Mi IMC es {bmi:.2f}."

    def exercise(self, minutes: int):
        """
        Simula que el humano hace ejercicio
        Args:
            minutes (int): Minutos de ejercicio
        """
        calories_burned = minutes * 5  # Asumimos 5 calorías por minuto
        self.weight = max(
            40, self.weight - (calories_burned / 7700)
        )  # 7700 calorías = 1kg
        print(
            f"{self.name} hizo {minutes} minutos de ejercicio y quemó {calories_burned} calorías."
        )


exca_dev = Human("Exca Dev", 22, 1.92, 62)
print(exca_dev.introduce())
print(exca_dev.calculate_bmi())
print(exca_dev.have_birthday())
print(exca_dev.exercise(10))
