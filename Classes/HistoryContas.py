from .Conta import Conta

class HistoryContas:
    def __init__(self) -> None:
        self.__contas = []
    def getMediaKw(self):
        pass
    def getValorMediaContas(self):
        pass
    def getMesMaiorConsumo(self):
        pass
    def getMesMenorConsumo(self):
        pass
    def setConta(self,conta:Conta):
        self.__contas.append(conta)