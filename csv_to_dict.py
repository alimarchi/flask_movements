nf = input("fichero: ")

f = open(nf, "r")

linea_cabeceras = f.readline()
cabeceras = linea_cabeceras.split(",")

linea = f.readline()
lista_dict = []
while linea != "":
    campos = linea.split(",")
    d = {}
    for clave, valor in zip(cabeceras, campos):
        d[clave] = valor
        lista_dict.append(d)
        linea = f.readline()

print(lista_dict)