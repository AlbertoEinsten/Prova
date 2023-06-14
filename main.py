from Classes import Conta,HistoryContas
from datetime import datetime as dt

if __name__ == "__main__":
    history = HistoryContas()
    C = Conta()

    history.setConta(Conta("1251",dt.strptime("01/06/2023","%d/%m/%Y"),"001",200.0,100))
    history.setConta(Conta("1252",dt.strptime("01/07/2023","%d/%m/%Y"),"002",250.0,150))
    history.setConta(Conta("1253",dt.strptime("01/08/2023","%d/%m/%Y"),"003",50.0,50))

    print(history.getMediaKw())
    print(history.getValorMediaContas())
    print(history.getMesMaiorConsumo())
    print(history.getMesMenorConsumo())