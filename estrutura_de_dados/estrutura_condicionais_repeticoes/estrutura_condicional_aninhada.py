conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial")
    else:
        print("Saldo insuficiente")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else: 
        print("Saldo insuficiente")

elif conta_especial:
    print("Conta especial selecionada")

else:
    print("Não foi possível identificar o tipo da conta. Entre em contato com o seu gerente")