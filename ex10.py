#O índice de massa corpórea (IMC) de uma pessoa é igual ao peso(em quilogramas) dividido pelo quadrado de sua altura (em metros). 
#Construa um programa que dados o peso e altura de uma pessoa, informe o valor de seu IMC

peso= float(input("Digite o peso em kg: "))
altura= float(input("Digite a altura em metros: "))
print(f"O valor do IMC é {peso / (altura ** 2):.2f}.")