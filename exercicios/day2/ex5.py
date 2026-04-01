# Número positivo ou negativo

print("Número positivo ou negativo")

num = float(input("Digite um numero negativo ou positivo: "))
if num > 0:
    print("Este é um número positivo")
elif num == 0:
    print("0 não é positivo nem negativo")
else:
    print("Este é um número negativo")
