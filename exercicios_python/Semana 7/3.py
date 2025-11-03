from math import factorial
from random import randint

a = randint(0, 20)
b = randint(0, 20)

fatorialA = factorial(a)
fatorialB = factorial(b)

def soma_fatorial(fatorialA, fatorialB):
    somaFatorial = fatorialA + fatorialB
    return somaFatorial


print(f'A = {a}')
print(f'B = {b}')
print(f'A soma dos fatoriais de B e A é {soma_fatorial(fatorialA, fatorialB)}')




