#A tab. Hash é uma estrutura de dados, na qua o endereço de um elemento é gerado através de uma função hash. Isso faz com que acessar os dados se torne mais rápido .

#Em python, o dicionário representa a implementação da tabela hash. Para criar um dicionário utilize "{}"

dictionary = {'Nome': 'Anna', 'Curso': 'Biologia', 'Idade': '19'}

print("dictionary['Nome'] : ", dictionary['Nome'])

print("dictionary['Curso']: ", dictionary['Curso'])

dictionary['Escola'] = 'IFMA'

print("IFMA" in dictionary)

#Atenção! As chaves do dicionário precisam ser únicas! Mas os valores não

dictionary['Nome'] = 'Arthur'

#wrong_dictionary = {'Nome': 'Anna', 'Nome' : 'Pedro'}
#print(wrong_dictionary)

#Criando um dicionario vazio
lista_telefonica = {}
print (type(lista_telefonica))


