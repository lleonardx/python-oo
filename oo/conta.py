
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self)) #referencia que encontra o objeto
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        print("Valor depositado.")
        self.__saldo += valor

    def __pode_sacar(self, valor_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_sacar <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            print("Valor sacado.")
            self.__saldo -= valor
        else:
            print("Valor {} passou o limite".format(valor))

    def transferir(self, valor, destino):
        print("Valor Transferido.")
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property #getter = get
    def limite(self):
        return self.__limite

    @limite.setter #a funcao + setter = set
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
       return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}