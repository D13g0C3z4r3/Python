from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        pass
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class pessoafisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico ()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls (numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def histotico(self):
        return self._histotico
    
    @property
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor + saldo

        if excedeu_saldo:
            print("Operacao falhou saldo insuficiente")

        elif valor > 01:
            self._saldo -= saldo
            print("Saque realizado")
            return True
        else:
            print("operacao falho valor inserido invalido")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("operacao realizada")
        else:
            print("operacao falhou valor invalido")
            return False
        return True

class conta_corrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    def sacar(self, valor):
        numero_saque = len(
            [transacao for transacao in self.histotico.transacoes if transacao["tipo"] == saque.__name__]
        )
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saque > self.limite_saque

        if excedeu_limite:
            print("operacao falhou, limite execedido ") 
        elif excedeu_saque:
            print("numero de saque exedido")
        else:
            return super(). sacar(valor)
        return False
    def __str__(self):
        return f"""
            agencia:{self.agencia}
            C/C:{self.numero}
            titulo:{self.cliente.nome}
        """
         
class historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacao(self):
        return self._transacoes
    
    def adicionar_trasacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "date":datetime.now().strftime
            }
        )

class transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass

class saque(transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        secesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_trasacao(self)
class depositar(transacao):
    def __init__(self, valor):
        self._valor = valor

        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            secesso_transacao = conta.depositar(self.valor)

            if sucesso_transacao:
                conta.historico.adicionar_transacao
        

        
