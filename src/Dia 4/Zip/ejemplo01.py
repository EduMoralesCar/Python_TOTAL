# Ejemplo: Muestra en pantalla frases como la del siguiente ejemplo: La capital de Alemania es Berlín
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]

combinacion = list(zip(capitales,paises))
for capitales,paises in combinacion:
    print(f"La capital de {paises} es {capitales}")
