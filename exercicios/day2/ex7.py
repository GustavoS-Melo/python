#Desconto especial

print("Desconto especial")
valor = int(input("Digite o valor do produto: "))
if valor > 100:
    print("O valor deste produto com 10% de desconto fica:", valor - (valor * 10 / 100))
else:
    print("Para este valor de produto, não possui desconto")