saldo = 1000
opcao = 's'


def sacar():
    verifica_saldo(receber_valor()) #Isso pode ser removido sem afetar o saque
    debita_saldo(receber_valor())
    print('Saque realixado com sucesso')


def receber_valor():
    valor = float(input('Digite um valor:'))
    return valor

def verifica_saldo(x):
    global saldo
    if x < saldo:
        return True
    else:
        return False
    
def debita_saldo(x):
    global saldo
    saldo -= x
    return saldo

lista_clientes = {'1':{'usuario':'Arthur','senha':'111'},
                  '2':{'usuario':'Matheus','senha':'222'},
                  '3':{'usuario':'João','senha':'333'},
                  '4':{'usuario':'Caio','senha':'444'}}

registro_cliente = input('Digite um registro: ')
if registro_cliente in lista_clientes:
    nome_cliente = input('Digite um nome: ')
    if lista_clientes[registro_cliente]['usuario'] == nome_cliente:
        senha_cliente = input('Digite um senha: ')
        if lista_clientes[registro_cliente]['senha'] == senha_cliente:
            print('Voce acessou')
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
        else:
                print('Senha incorreta')
    else:
        print('Cliente não registrado')   
else:
    print('Não registrado')
    cliente_registro = input('Digite um registro: ')
    cliente_nome = input('Digite um nome: ')
    cliente_senha = input('Digite um senha: ')

    lista_clientes[cliente_registro] = {'usuario' : cliente_nome, 'senha' : cliente_senha}
    print('Seja bem vindo(a)', cliente_nome,'.')
    print(lista_clientes)