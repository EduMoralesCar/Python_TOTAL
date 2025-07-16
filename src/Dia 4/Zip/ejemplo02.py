
# Ejemplo: Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ['Apple', 'Dell', 'HP', 'Lenovo', 'Asus', 'Microsoft']
productos = ['MacBook Air (M1, M2)', 'Alienware (m15, x17)', 'Pavilion', 'ThinkPad (X1 Carbon, T Series)', 'VivoBook Series', 'Surface Laptop (Go, Studio)']

mi_zip = zip(marcas,productos)

for marcas,productos in mi_zip:
    print(f"La marca: {marcas}\n \tTiene como producto:\t{productos}")