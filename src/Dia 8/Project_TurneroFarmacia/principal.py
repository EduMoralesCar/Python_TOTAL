from numeros import (
    siguiente_farmacia,
    siguiente_perfumeria,
    siguiente_cosmetica
)

def elegir_area():
    print("Bienvenido al sistema de turnos de la farmacia.")
    print("Áreas disponibles:")
    print("1. Farmacia")
    print("2. Perfumería")
    print("3. Cosmética")

    opcion = input("Seleccione el área (1/2/3): ")

    if opcion == '1':
        print("Bienvenido al sistema de turnos de la farmacia")
        print(siguiente_farmacia())
    elif opcion == '2':
        print("Bienvenido al sistema de turnos de la perfumería")
        print(siguiente_perfumeria())
    elif opcion == '3':
        print("Bienvenido al sistema de turnos de la cosmética")
        print(siguiente_cosmetica())
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

def main():
    continuar = "s"
    while continuar.lower() == "s":
        elegir_area()
        continuar = input("¿Desea solicitar otro turno? (s/n): ")
    print("Gracias por usar el sistema de turnos. ¡Hasta luego!")
if __name__ == "__main__":
    main()