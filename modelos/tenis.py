class Tenis:
    tenis_lista = []

    def __init__(self, marca, modelo, cor, tamanho):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.tamanho = tamanho
        self.ativo = False
        Tenis.tenis_lista.append(self)

    def __str__(self):
        return f'{self.marca} | {self.modelo} | {self.cor} | {self.tamanho} | {"Ativo" if self.ativo else "Inativo"}'

    def listar_tenis(cls):
        for tenis in cls.tenis_lista:
            print(tenis)


tenis1 = Tenis('Nike ', 'Air Max', 'Preto', '42')
tenis2 = Tenis('Adidas', 'Superstar', 'Branco', '40')
tenis3 = Tenis('Puma', 'Ignite', 'Azul', '44')


Tenis.listar_tenis()
