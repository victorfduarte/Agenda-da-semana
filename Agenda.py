import reader
from Dia import Dia
from Tarefa import Tarefa


class Agenda:
    def __init__(self, base_file: str):
        self.__dias = ()

        base = reader.load(base_file)
        for d in base:
            dia = Dia(d["dia"])

            for t in d["tarefas"]:
                tarefa = Tarefa(t["titulo"], t["horario"])
                dia.add_tarefa(tarefa)
            
            self.__dias += (dia,)
    

    def getDia(self, dia: int) -> Dia:
        for d in self.__dias:
            if d.get_num() == dia:
                return d
        else:
            return Dia(dia)
    
    def getDias(self) -> tuple:
        return self.__dias