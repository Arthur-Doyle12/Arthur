saldo = 1000
opcao = 's'
while opcao == 's':
    print('Digite o numero de operação.')
    print('[1] - Sacar')
    print('[2] - Depositar')
    print('[3] - Saldo')
    print('[4] - Falar com gerente')
    print('[0] - Encerrar')
    numero = float(input(''))
    match numero:
        case 1:
            print('Quanto deseja sacar?')
            saque = float(input())
            if saque > saldo:
                print('Saque não realizao, invalido.')
            else:
                print('Saque realizado com sucesso.')
                saldo -= saque
                print('saldo final: ',saldo)
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
        case 0:
            opcao = 'n'