mi_archivo = open('registro.txt', 'a')

registro_ultima_sesion = ["Edomocar",'\t', "05/08/2025",'\t', "05:55:35 hs",'\t', "Sin errores de carga\n"]
mi_archivo.writelines(registro_ultima_sesion)

mi_archivo.close()

mi_archivo = open('registro.txt', 'r')
print(mi_archivo.read())

mi_archivo.close()