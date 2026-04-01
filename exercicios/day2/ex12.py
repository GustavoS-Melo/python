# Pode dirigir?

print("Você Pode dirigir?")

idade = int(input("Qual sua idade?: "))
cnh = input("você possui CNH?: ")

if idade >= 18 and cnh == "sim":
    print("Parabéns, você pode dirigir!")
else:
    print("Você ainda não pode dirigir")