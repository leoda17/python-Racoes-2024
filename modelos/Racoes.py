from modelos.valor import Valor

class RacoesESementes:
    produtos = []

    def __init__(self, nome, tipo, categoria, local):
        self._nome = nome.upper()
        self._tipo = tipo.title() 
        self._categoria = categoria.title() 
        self._local = local.title()
        self._estoque = False
        self._valor = []
        RacoesESementes.produtos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._tipo} | {self._categoria} | {self._local} | {self.estoque}'

    @classmethod
    def listar_produtos(cls):
        print('''

█▀█ ▄▀█ █▀▀ █▀█ █▀▀ █▀   █▀▀   █▀▀ █ ▄▀█
█▀▄ █▀█ █▄▄ █▄█ ██▄ ▄█   ██▄   █▄▄ █ █▀█
        ''')

        print(f'{"Nome do Produto".ljust(20)} | {"Tipo".ljust(20)} | {"Categoria".ljust(20)} | {"Local".ljust(20)} | {"Estoque".ljust(20)} | {"Média de Preço".ljust(20)}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for produto in cls.produtos:
            print(f'{produto._nome.ljust(20)} | {produto._tipo.ljust(20)} | {produto._categoria.ljust(20)} | {produto._local.ljust(20)} | {produto.estoque.ljust(20)} | {produto.media_preço}')
            print('------------------------------------------------------------------------------------------------------------------------------')

    @property
    def estoque(self):
        return '❌ Sem estoque' if self._estoque else '✔️ Em estoque'

    def alterar_estado(self):
        self._estoque = not self._estoque        

    def receber_preço(self, fornecedor, preço):
        preço = Valor(fornecedor, preço)
        self._valor.append(preço)

    @property
    def media_preço(self):
        if not self._valor:
            return 0 
        somas_dos_preços = sum(valor._preço for valor in self._valor)
        quantidade_fornecedores = len(self._valor)
        media = round(somas_dos_preços / quantidade_fornecedores, 1)
        return media
