# EXEMPLO 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)


# EXEMPLO 2
numeros_2 = [1, 30, 21, 2, 9, 65, 34]
quadrado_2 = [numero ** 2 for numero in numeros_2]
print(quadrado_2)