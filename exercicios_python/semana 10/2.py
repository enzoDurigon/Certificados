conta = {'transações': 0, 'saldo': 1000, 'media': 0}
print(conta)

valor_compra = 100
conta['saldo'] -= valor_compra
conta['transações'] += 1
conta['media'] = (conta['media'] * (conta['transações'] - 1) + valor_compra) / conta['transações']

valor_compra = 200
conta['saldo'] -= valor_compra
conta['transações'] += 1
conta['media'] = (conta['media'] * (conta['transações'] - 1) + valor_compra) / conta['transações']


print(conta)
