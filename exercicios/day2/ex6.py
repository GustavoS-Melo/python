#Comparação de três números

print("Comparação de três números")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print("O maior valor dos números digitados foi o 1º")
elif num2 > num1 and num2 > num3:
    print("O maior valor dos números digitados foi o 2º")
else:
    print("O maior valor dos números digitados foi o 3º")

