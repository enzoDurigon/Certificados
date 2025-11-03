telheiro = int(input('Quantos pregos telheiros foram vendidos nesse dia?: '))
quadrado = int(input('Quantos pregos quadrados foram vendidos nesse dia?: '))


def arrecadacao_telheiro(telheiro):
    valorTelheiro = telheiro * 1.05
    return valorTelheiro

def arrecadacao_quadrado(quadrado):
    valorQuadrado = quadrado * 0.51
    return valorQuadrado

totalArrecadado = arrecadacao_telheiro(telheiro) + arrecadacao_quadrado(quadrado)
comissao = totalArrecadado * 0.1


print(f'Valor da venda de pregos telheiros: R$ {arrecadacao_telheiro(telheiro)}')
print(f'Valor da venda de pregos quadrados: R$ {arrecadacao_quadrado(quadrado)}')
print(f'Total arrecadado: R$ {totalArrecadado}')
print(f'Comissao: R$ {comissao}')


