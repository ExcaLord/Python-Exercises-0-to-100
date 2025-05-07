class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error: Division por cero"
        return a / b


# Uso de la Calculadora
calc = Calculadora()
operation = input("Que operacion desea realizar? ")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if operation == "suma":
    print(f"Suma: {calc.suma(a, b)}")
elif operation == "resta":
    print(f"Resta: {calc.resta(a, b)}")
elif operation == "multiplicacion":
    print(f"Multiplicación: {calc.multiplicacion(a, b)}")
elif operation == "division":
    print(f"División: {calc.division(a, b)}")
else:
    print("Operación inválida")
