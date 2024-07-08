def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo(nome):
    print ("Olá {nome}!")


ola_mundo()