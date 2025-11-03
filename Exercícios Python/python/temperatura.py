resposta = 'sim'
soma = quantidade = media = maior = menor = 0
while resposta in 'sim':
    temperatura = int(input('Digite uma temperatura: '))
    soma += temperatura
    quantidade += 1
    if quantidade == 1:
        maior = menor = temperatura
    else:
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura

    resposta = str(input('Quer continuar? [SIM OU NAO]: ')).lower().split() [0]
media = soma / quantidade

print(f"A maior temperatura registrada foi {maior} C.")
print(f"A menor temperatura registrada foi {menor} C.")
print(f"A media das temperaturas e {media:.1f} C.")