class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nmr_patas):
        super().__init__(cor_pelo=cor_pelo,cor_bico=cor_bico, nmr_patas=nmr_patas)


gato = Gato(nmr_patas = 4, cor_pelo="branco")
print(gato)

ornitorrinco = Ornitorrinco(nmr_patas=4, cor_pelo="marrom", cor_bico="amarelo")
print(ornitorrinco)