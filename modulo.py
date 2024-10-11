saldo = 1000

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
        print('Saldo atual: ', saldo)


def deposito():
    global saldo
    print('Qunato deseja depositar?')
    deposito = float(input())
    print('Deposito realizado com sucesso.')
    saldo += deposito
    print('Saldo final:',saldo)