saldo = 1000
opcao = 's'


def sacar():
    debita_saldo(receber_valor())
    


def receber_valor():
    valor = float(input('Digite um valor:'))
    return valor    
    
def debita_saldo(x):
    global saldo
    if x <= saldo:
        saldo -= x
        print('Saque realixado com sucesso')
        print('Saldo atual: ', saldo)
    else:
        print('Saldo insuficiente')
    

lista_clientes = {'1':{'nome': 'Arthur Doyle', 'usuario':'Arthur','senha':'111111'},
                  '2':{'nome': 'Matheus Kellyton', 'usuario':'Matheus','senha':'222222'},
                  '3':{'nome': 'João Brega', 'usuario':'João','senha':'333333'},
                  '4':{'nome': 'Caio Guimares', 'usuario':'Caio','senha':'444444'}}

cpf_cliente = input('Digite seu cpf: ')
if cpf_cliente in lista_clientes:
    nome_cliente = input('Digite um nome: ')
    if lista_clientes[cpf_cliente]['usuario'] == nome_cliente:
        senha_cliente = input('Digite um senha: ')
        if lista_clientes[cpf_cliente]['senha'] == senha_cliente:
            print('Voce acessou')
            print('Seja bem vindo(a)', nome_cliente)
        else:
                print('Senha incorreta')
    else:
        print('Cliente não registrado')   
else:
    print('Não registrado')
    cliente_cpf = input('Digite um cpf: ')
    cliente_nome = input('Digite um nome: ')
    cliente_senha = input('Digite um senha: ')
    senha = len(cliente_senha)

    if senha >= 6:
        usuario = cliente_nome.split()
        cliente_usuario = usuario[0].capitalize()

        lista_clientes[cliente_cpf] = {'nome': cliente_nome, 'usuario' : cliente_usuario, 'senha' : cliente_senha}
        print('Seja bem vindo(a)', cliente_usuario,'.')
        print(lista_clientes)
    else:
        print('Digite uma senha com mais de 6 números')

while opcao == 's':
                    print('Digite o numero de operação.')
                    print('[1] - Sacar')
                    print('[2] - Depositar')
                    print('[3] - Saldo')
                    print('[4] - Falar com gerente')
                    print('[5] - Adicionar cliente')
                    print('[0] - Encerrar')
                    numero = float(input(''))
                    match numero:
                        case 1:
                            print('Quanto deseja sacar?')
                            sacar()
                        case 2:
                            print('Qunato deseja depositar?')
                            deposito = float(input())
                            print('Deposito realizado com sucesso.')
                            saldo += deposito
                            print('Saldo final:',saldo)
                        case 3:
                            print(saldo)
                        case 4:
                            print('Chamando gerente, por favor aguarde...')
                        case 5:
                            nome = input('Nome do cliente:')
                            lista_clientes.append(nome)
                            print(lista_clientes)
                        case 0:
                            opcao = 'n'