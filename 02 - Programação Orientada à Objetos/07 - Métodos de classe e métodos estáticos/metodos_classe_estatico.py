class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
p = Pessoa.criar_data_de_nascimento(2002, 8, 8, "Leandro")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(18))