# 18. Faça um programa que peça o tamanho de um arquivo
# para download (em MB) e a velocidade de um link de
# Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este
# link (em minutos).

arquivo = float(input("Informe o tamanho do arquivo em MB: "))
velocidade = float(input("Informe a velocidade do link de internet em Mbps: "))

velocidade_mega = velocidade / 8
tempo_minuto = ((arquivo / velocidade_mega) / 60)

print("O tempo de download do arquivo é de %.1f" %tempo_minuto, "minutos")