lista1 = ['a', 'b', 'c']
resultado1 = len(lista1)
print(resultado1)

#lista de ordenar de forma asc (alfabetico y numerico)
lista2 = [9,8,7,6,5,3,4,2,1,0]
lista2.sort()
print(lista2)

#inversion del orden en forma desc (alfabetico y numerico)
lista3 = [0,1,2,3,4,5,6,7,8,9]
lista3.reverse()
print(lista3)

#ejemplos agregar "motocicleta"
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append( "motocicleta")
print(medios_transporte)

#eliminar un obejeto de las listas: ejemplo de quitar el tercer elemento
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
print("\nAlmacen de frutas:\n ")
print(frutas)

eliminado = frutas.pop(2)
print("\nUn elemento fue eliminado: " + eliminado + '\n')
print(frutas)