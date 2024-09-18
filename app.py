from modelos.Racoes import RacoesESementes

racao_bovino = RacoesESementes('Ração Bovinos', 'Ração', 'Bovinos', 'Morumbi')
racao_quino = RacoesESementes('Ração Quinos', 'Ração', 'Quinos', 'Vila A')
semente_milho = RacoesESementes('Semente de Milho', 'Semente', 'Milho', 'Centro')
racao_bovino.alterar_estado()


semente_milho.receber_preço('Farma do Campo', 45.5)
semente_milho.receber_preço('Agropecuária do Sul', 44.0)
semente_milho.receber_preço('Sementes do Norte', 46.0)

def main():
    RacoesESementes.listar_produtos()

if __name__ == '__main__':
    main()
