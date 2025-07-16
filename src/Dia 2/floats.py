# Ejemplo de uso de tipos de datos en Python con floats
print("*************CUANTOS AÑOS TIENES ***************")
print()
edad = input("Menciona tu edad: ")
edad = int(edad)
print("El tipo de Dato es: "+ str(type(edad)))
print()

nueva_edad = edad + 1

#Mostrar las Edad actual y posterior
print(f"Tu edad actual es {edad} años y el Proximo año cumpliras {nueva_edad} años")

