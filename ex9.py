#Faça um programa que dadas as medidas de uma sala em metro (comprimento e largura), bem como o preço do metro quadrado do carpete,
#informe o custo total para forrar o piso da sala

comprimento = float(input("Digite o comprimento da sala em metros: "))
largura = float(input("Digite a largura da sala em metros: "))
preco_carpete = float(input("Digite o preço do metro quadrado do carpete: "))
print(f"O custo total para forrar o piso da sala é de R${(comprimento * largura) * preco_carpete:.2f}.")