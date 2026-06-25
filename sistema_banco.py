saldo = 1000
depositos = []
saques = []

#funções
def depositar(saldo):
    deposito = int(input("Qual valor você quer depositar ?"))
    while deposito <= 0:
        print("Valor invalido para a operação tente novamente")
        deposito = int(input("Qual valor você quer depositar ?"))
    saldo = saldo + deposito
    depositos.append(+deposito)
    print(f"Você depositou R${deposito} reais")
    return saldo


def sacar(saldo):
    saque = int(input("Qual valor você quer sacar ?"))
    while saque <= 0 or saque > saldo:
        print("valor invalido para a operação")
        saque = int(input("Qual valor você quer sacar ?"))
    saldo = saldo - saque
    saques.append(-saque)
    print(f"Você sacou R${saque} reais")
    return saldo
    

print("Olá, seja bem vindo ao banco Rings, o que deseja fazer hoje ?")
print("1 - Depositar")
print("2 - Sacar")
print("3 - Verificar saldo")
print("4 - Extrato")
print("5 - Sair")
while True:
    opção = int(input("Digite a operação desejada: "))
    if opção == 1:
        saldo = depositar(saldo)
    elif opção == 2:
        saldo = sacar(saldo)
    elif opção == 3:
        print(f"Seu saldo atual é de R${saldo} reais")
    elif opção == 4:
        print("Extrato de depósitos:")
        print(depositos)
        print("Extrato de saques:")
        print(saques)
    elif opção == 5:
        print("Obrigado por utilizar o banco Rings, volte sempre !")
        break