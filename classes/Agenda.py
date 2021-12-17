import reader
from classes.Dia import Dia
from classes.Tarefa import Tarefa


class Agenda:
    def __init__(self, base_file):
        self.__dias = ()

        base = reader.load(base_file)
        for d in base:
            dia = Dia(d["dia"])

            for t in d["tarefas"]:
                tarefa = Tarefa(t["titulo"], t["horario"])
                dia.add_tarefa(tarefa)
            
            self.__dias += (dia,)
        
        print(self.__dias)

    

    def getDia(self, dia: int):
        return self.dias[dia]
    
    def getDias(self):
        return self.dias