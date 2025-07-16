'''
Atajo para dar formato en PyCharm
Windows/Linux: Ctrl + Alt + L
'''

dic = {'clave1': 101, 'clave2': 102}

a = dic.popitem()
print(a)
print(dic)

# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando el método insert():
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
fruta_agregada = frutas.insert(3, 'naranja')
print(frutas)

'''Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común),
utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

Método isdisjoint():
Comprueba si los dos conjuntos son disjuntos, es decir, si no tienen elementos en común.
Retorna True si no hay elementos comunes; de lo contrario, False.
'''
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

verificacion_productos = marcas_tv.isdisjoint(marcas_smartphones)
print(verificacion_productos)
