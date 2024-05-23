# EXEMPLO 1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)


# EXEMPLO 2

numeros_2 = [1, 30, 21, 2, 9, 65, 34]
pares_2 = [numero for numero in numeros if numero % 2 == 0]
print(pares_2)
