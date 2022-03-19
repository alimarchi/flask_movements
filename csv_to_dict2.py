import csv

nombref = input("fichero: ")

f = open(nombref, "r")
dreader = csv.DictReader(f, delimiter=",", quotechar='"')

lista_movimientos = []

for fila in dreader:
    lista_movimientos.append(fila)

print(lista_movimientos)