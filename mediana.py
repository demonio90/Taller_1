print("Datos a tratar: ")
data = [1, 4, 6, 7, 2, 3, 4, 7, 1, 2, 4, 3, 4, 5,
        6, 5, 2, 3, 1, 2, 5, 6, 7, 3, 4, 1, 5, 7,
        1, 7, 6, 5, 3, 4, 3, 4, 5, 5, 5, 6, 7, 3,
        4, 5, 3, 4, 5, 4, 5, 6, 3, 4, 3, 4, 5, 3,
        4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 1, 3,
        4, 5, 3, 4, 5, 6, 5, 4, 6, 5, 6, 5, 1, 7]

print(data)
dOrder = sorted(data)

n = len(dOrder)
middle = int(n / 2)

#Calculo de la mediana
if n % 2 == 0:
    mediana = (dOrder[middle + 1] + dOrder[middle + 2]) / 2
else:
    mediana = dOrder[middle + 1] * 1

print('')
print('Total datos', n)
print('Mediana: ', mediana)