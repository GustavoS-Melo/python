# Sistema simples de login

print("Sistema simples de login")

login = "joao123"
senha = "123456"

usurarioLogin = input("Digite seu login: ")
usurarioSenha = input("Digite sua senha: ")

if usurarioLogin == login and usurarioSenha == senha:
    print("Login aprovado!")
elif usurarioLogin == login and usurarioSenha != senha:
    print("Senha incorreta!")
elif usurarioLogin != login and usurarioSenha == senha:
    print("Login incorreto!")