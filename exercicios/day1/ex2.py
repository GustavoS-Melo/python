#Idade em dias:

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
dias = 365
print('Olá', nome, 'sua idade convertida de anos para dias é:', idade * dias, 'dias')
# Sempre que usar input(), o Python entende o dado como texto (string). 
# Se precisar fazer cálculos, converta para int() ou float().