"""Este programa deve retornar o usuário e o 
domínio de um dado email."""

email = input("Qual o seu email?\n")

usuario = email[:email.index('@')]

dominio = email[email.index('@') + 1:]

print(f'Seu usuário é {usuario} com o domínio {dominio}')