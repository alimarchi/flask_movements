import csv

nombref = input("fichero: ")

f = open(nombref, "r")

freader = csv.reader(f, delimiter=",", quotechar='"')

lista_movimientos = []

for fila in freader:
    lista_movimientos.append(fila)

print(lista_movimientos)