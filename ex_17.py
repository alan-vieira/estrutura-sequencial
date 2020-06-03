# 17. Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da
# tinta é de 1 litro para cada 6 metros quadrados e que
# a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros,
# que custam R$ 25,00.
#
# -Informe ao usuário as quantidades de tinta a
# serem compradas e os respectivos preços em 3 situações:
#
# -comprar apenas latas de 18 litros;
# -comprar apenas galões de 3,6 litros;
# -misturar latas e galões, de forma que o preço
# seja o menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é,
# considere latas cheias.
# não terminado


comodo = int(input("Informe o tamanho do cômodo em metros quadrados: "))
litro = comodo / 6

preco_galao = 80.0
capacidade_galao = 18
preco_lata = 25.0
capacidade_lata = 3.6

galao = round(litro / capacidade_galao)
total1 = (galao * preco_galao)
lata = round(litro / capacidade_lata)
total2 = (lata * preco_lata)

print(litro)
print("Você precisará de", galao, "lata(s) grande(s)")
print("O preço total é de: R$", total1)
print()
print("Você precisará de", lata, "lata(s) pequena(s)")
print("O preço total é de: R$", total2)