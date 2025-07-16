texto1 = "Welcome to the world of Python development"

#texto en MAYUSCULA
resultado1 = texto1.upper()
print(resultado1)

#texto en MINUSCULA
resultado2 = texto1.lower()
print((resultado2))

#texto en separación
resultado3 = texto1.split()
print(resultado3)

resultado4 = texto1.split("e") #sepacion desde la letra "e"
print(resultado4)

#Texto para remplazar
texto2 = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado5 = texto2.replace("difícil","fácil")
resultado6 = texto2.replace("mala","buena")
print(resultado5 + "\n" + resultado6)

# metodo de String JOIN
a = "Bienvenido"
b = "al mundo"
c = "del Desarrollo"
d = "en Python"
e = " ".join([a,b,c,d])

print(e)

# Separando elementos con un espacio
lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(["La","legibilidad","cuenta."])
print(resultado)

# Texto para remplazar
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado11 = frase.replace("difícil","fácil")
resultado22 = resultado11.replace("mala","buena")
print(resultado22)