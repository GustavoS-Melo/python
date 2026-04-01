# Ano bissexto simples

print("Ano bissexto simples")

ano = int(input("Digite o ano em questão: "))
if ano % 4 == 0:
    print("Este ano é bissexto")
else:
    print("Este ano não é bissexto")