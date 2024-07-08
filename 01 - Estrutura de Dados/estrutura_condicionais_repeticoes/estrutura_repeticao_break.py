while True:
    numero = int(input("Informe um número inteiro: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)