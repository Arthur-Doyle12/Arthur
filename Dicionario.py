dicionario = {'Nome':'Arthur','Idade':24,'Nacionalidade':'Brasileiro','Sexo':'Masculino','Estado Civil':'Solteiro'}
print(dicionario)

chaves = dicionario.keys()
print(chaves)

valores = dicionario.values()
print(valores)

for chave,valor in dicionario.items():
    print(chave,':',valor)
    print(f'{chave}:{valor}')

print(dicionario['Nome'])

dicionario_1 = dicionario['Idade']
print(dicionario_1)

profissao = dicionario.get('profissão', 'Não especificado')

print(profissao)

print(dicionario[input('')])

dicionario['Ocupação'] = 'Estudante'

dicionario['Idade'] = 100

estado_civil = dicionario.pop('Estado Civil')

dicionario.pop('Nacionalidade')

print(dicionario)
print(estado_civil)



del dicionario

clientes = {
    '999':{'user':'Chico','pass':123}
}

codigo_cliente = input('Digite um codigo: ')
nome_cliente = input('Digite seu usuario: ')
senha_cliente = input('Digite sua senha: ')

clientes[codigo_cliente] = {'user':nome_cliente, 'pass':senha_cliente}

print(clientes)

