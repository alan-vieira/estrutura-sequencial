# 16. Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que
# a cobertura da tinta é de 1 litro para cada 3 metros
# quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades
# de latas de tinta a serem compradas e o preço total.

comodo = int(input("Informe o tamanho do cômodo em metros quadrados: "))
litro = comodo / 3

preco_lata = 80.0
capacidade_lata = 18

lata = round(litro / capacidade_lata)
total = (lata * preco_lata)

print(litro)
print("Você precisará de", lata, "lata (s)")
print("O preço total é de: R$", total)