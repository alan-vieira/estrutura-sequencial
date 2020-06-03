# 11. Faça um Programa que peça 2 números inteiros
# e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

num1 = int(input("digite um número inteiro: "))
num2 = int(input("digite outro número inteiro: "))
num3 = float(input("digite um número real: "))

print("O produto do dobro do primeiro com metade do segundo é igual a", (2*num1) * (num2/2))
print("A soma do triplo do primeiro com o terceiro é igual a", (3*num1) + num3)
print("O terceiro elevado ao cubo é igual a", num3 ** 3)