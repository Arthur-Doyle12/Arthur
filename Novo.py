saldo = 1000
opcao = 's'
lista_clientes = ['Arthur','Matheus','João','Caio']

cliente = input('Digite seu nome:')
if cliente in lista_clientes:
    print('Seja bem vindo(a)', cliente)
else:
    print('Cliente não registrado.')
    opcao = 'n'

def sacar():
    verifica_saldo(receber_valor())
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