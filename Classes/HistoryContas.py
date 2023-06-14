from .Conta import Conta

class HistoryContas:
    def __init__(self) -> None:
        self.__contas = []

    def getMediaKw(self)-> str:
        media = 0
        for conta in self.__contas:
           #print(conta.getDadosConta()) 
           media +=conta.getKwGasto()
        return f'Media de kw = Kw{media/len(self.__contas)}'
            
    def getValorMediaContas(self)-> str:
        media = 0
        for conta in self.__contas:
            media += conta.getValorPagar()
        return f"Media valor = R${media/len(self.__contas):.2f}"

    def getMesMaiorConsumo(self)-> str:
        maior = self.__contas[0]
        for conta in self.__contas:
            if maior.getKwGasto() <= conta.getKwGasto():
                maior = conta
        return f"Data maior consumo = {maior.getDataLeitura()}"

    def getMesMenorConsumo(self)-> str:
        menor = self.__contas[0]
        for conta in self.__contas:
            if menor.getKwGasto() >= conta.getKwGasto():
                menor = conta
        return f"Data menor consumo = {menor.getDataLeitura()}"
    def setConta(self,conta:Conta)-> None:
        self.__contas.append(conta)