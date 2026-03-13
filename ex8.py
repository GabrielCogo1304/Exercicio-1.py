#Elabore um programa que dada uma distância percorrida (em quilômetros), bem como o total de combustível gasto (em litros), informe o consumo do veículo
distancia = float(input("Digite a distância percorrida em quilômetros: "))
combustivel = float(input("Digite o total de combustível gasto em litros: "))
print(f"O consumo do veículo é de {distancia / combustivel} km/l.")