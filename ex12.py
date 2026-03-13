#Elabore um programa que faça a simulação de um caixa de uma loja. O usuário deverá digitar o Valor da Compra, o Valor Pago pelo cliente.
#O programa irá retornar o valor do troco, as cédulas que fazem parte do troco e a quantidade de cada cédula.
#Para este programa considere as cédulas de R$100, R$50, R$20, R$10, R$5 e R$1 real sem if ou else sem len
#Considere a possibilidade de não haver troco
#Exemplo: Valor da compra R$ 354.00, valor pago R$ 637.00, o troco é R$ 283.00,

valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago pelo cliente: "))
troco = valor_pago - valor_compra
nota100= troco // 100
nota50= (troco % 100) // 50
nota20= (troco % 50) // 20
nota10= (troco % 20) // 10
nota5= (troco % 10) // 5
nota1= troco % 5
print(f"O valor do troco é R${troco:.2f}.")
