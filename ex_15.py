# 15. Faça um Programa que pergunte quanto você ganha
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de
# Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido,
# conforme a tabela abaixo:
#
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

salario_hora = float(input("Quanto você ganha por hora: "))
hora_trabalhada = float(input("Quantas horas você trabalhou nesse mês: "))

salario_bruto = salario_hora * hora_trabalhada * 30
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - (ir + inss + sindicato)

print("Salário bruto: R$", salario_bruto)
print("Desconto do IR: R$", ir)
print("Desconto do INSS: R$", inss)
print("Desconto do Sindicato: R$", sindicato)
print("Salário líquido: R$", salario_liquido)