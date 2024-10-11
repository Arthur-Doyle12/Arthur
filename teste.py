lista_clientes = {'1':{'usuario':'Arthur','senha':'111'},
                  '2':{'usuario':'Matheus','senha':'222'},
                  '3':{'usuario':'João','senha':'333'},
                  '4':{'usuario':'Caio','senha':'444'}}

registro_cliente = input('Digite um registro: ')
nome_cliente = input('Digite um nome: ')


if lista_clientes[registro_cliente]['usuario'] == nome_cliente:
    senha_cliente = input('Digite um senha: ')
    if lista_clientes[registro_cliente]['senha'] == senha_cliente:
        print('Voce acessou')
    else:
            print('Senha incorreta')
else:
    print('Cliente não registrado')