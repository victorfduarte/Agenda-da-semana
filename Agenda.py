from Dia import Dia
from Tarefa import Tarefa


class Agenda:
    def __init__(self, struct: list):
        self.__dias = []

        for d in struct:
            dia = Dia(d["dia"])

            for t in d["tarefas"]:
                tarefa = Tarefa(t["titulo"], t["horario"])
                dia.add_tarefa(tarefa)
            
            self.__dias.append(dia)
    

    def getDia(self, dia: int) -> Dia:
        '''Retorna o dia: Dia correspondente ao número (0 - Domingo, 1 - Segunda...)'''
        for d in self.__dias:
            if d.get_num() == dia:
                return d
        else:
            return Dia(dia)
    

    def getDias(self) -> tuple:
        '''Retorna a lista de todos os dias: Dia'''
        return self.__dias
    

    def addDia(self, dia: Dia):
        '''Adiciona um dia à lista de todos os dias'''
        self.__dias.append(dia)