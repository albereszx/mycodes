Desenvolvi um código em Python, através de estudos em criação de classes; no qual simula uma conta bancária,
com istâncias (Deposito e Saque).

#CODIGO ABAIXO :


class Conta:

    def __init__(self,titular, saldo, banco) :
        self.titular = titular
        self.saldo = saldo
        self.banco = banco


    def adc(self):
        pergunta1 = (input("Gostaria de fazer um depósito?" ))
        if pergunta1 =="sim":
            deposito = int(input("Qual o valor do depósito ?"))
            self.saldo += deposito
        return self.saldo
    

    def sub(self):
        pergunta = (input('Gostaria de fazer um saque?'  ))
        if pergunta =="sim":
            saque = int(input('Qual o valor do saque ?'))
            if saque > saldo :
                print('Saldo indisponível)
            else:

                self.saldo -= saque
        return self.saldo
        

    def mostra(self):
        print (f'Seu saldo em {banco} é {self.saldo:.2f} Reais')

titular = input("Qual o nome do titular da conta ? " )
saldo = int(input("Quanto tem disponível na conta ? "))
banco = input("A qual banco a conta pertence? ")

conta = Conta(titular,saldo,banco)

conta.adc()
conta.sub()
conta.mostra()
