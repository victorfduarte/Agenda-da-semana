class Agenda:
    def __init__(self):
        self.dias = (Dia('Domingo'), Dia('Segundo'), Dia('Terça'), Dia('Quarta'),
                     Dia('Quinta'), Dia('Sexta'), Dia('Sábado'))
    

    def getDia(self, dia):
        return self.dias[dia]


class Dia:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def getTarefas(self):
        return self.tarefas
    
    def addTarefa(self, nome):
        self.tarefas.append(nome)
    
    def removeTarefa(self, index):
        self.tarefa.pop(index)