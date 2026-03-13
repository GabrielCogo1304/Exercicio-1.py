#Uma certa importância será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
#• O primeiro ganhador recebera 46%;
#• O segundo recebera 32%;
#• O terceiro recebera o restante;
#Elabore um programa que dado o valor do concurso em reais ele, calcule e imprima a quantia ganha por cada um dos ganhadores

valor_concurso = float(input("Digite o valor do concurso em reais: "))
print(f"O primeiro ganhador receberá R${valor_concurso * 0.46:.2f}, o segundo ganhador receberá R${valor_concurso * 0.32:.2f} e o terceiro ganhador receberá R${valor_concurso * 0.22:.2f}.")
