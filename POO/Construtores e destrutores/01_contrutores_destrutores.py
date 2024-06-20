class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo instância da classe.")

    def latir(self):
        print("auau")

c = Cachorro("Nina", "preto e branco")
c.latir()