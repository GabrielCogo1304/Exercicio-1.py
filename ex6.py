#Leia o salário mensal atual de um funcionário e o percentual de reajuste e determine o valor do novo salário

salario = float(input("Digite o salário mensal atual do funcionário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))
print(f"O valor do novo salário é {salario + (salario * percentual_reajuste / 100)}.")