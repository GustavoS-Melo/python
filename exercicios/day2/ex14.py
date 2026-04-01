# Calculadora com escolha

print("Calculadora com escolha")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operação = input("Digite qual operação deseja: ")

if operação == "+":
    print(num1 + num2)
elif operação == "-":
    print(num1 - num2)
elif operação == "*":
    print(num1 * num2)
elif operação == "/":
    print(num1 / num2)
else:
    print("Digite um operador valido")