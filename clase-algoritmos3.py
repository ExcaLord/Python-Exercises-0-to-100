def convertir_temperatura(temperatura, unidad_origen, unidad_destino):
    if unidad_origen.lower() == "celsius":
        if unidad_destino.lower() == "fahrenheit":
            return (temperatura * 9 / 5) + 32
        elif unidad_destino.lower() == "kelvin":
            return temperatura + 273.15
        else:
            return "Unidad de destiino no valida"
    elif unidad_origen.lower() == "fahrenheit":
        if unidad_destino.lower() == "celsius":
            return (temperatura - 32) * 5 / 9
        elif unidad_destino.lower() == "kelvin":
            return (temperatura - 32) * 5 / 9 + 273.15
        else:
            return "Unidad de destiino no valida"
    elif unidad_origen.lower() == "kelvin":
        if unidad_destino.lower() == "celsius":
            return temperatura - 273.15
        elif unidad_destino.lower() == "fahrenheit":
            return (temperatura - 273.15) * 9 / 5 + 32
        else:
            return "Unidad de destino no valida"


if __name__ == "__main__":
    temp = float(input("Ingrese la temperatura: "))
    unidad_origen = input("Ingrese la unidad de origen: celsius, kelvin, fahrenheit")
    unidad_destino = input("Ingrese la unidad de destino: celsius, kelvin, fahrenheit")
    resultado = convertir_temperatura(temp, unidad_origen, unidad_destino)
    print(f"{temp} grados {unidad_origen} son {resultado} grados {unidad_destino}")
