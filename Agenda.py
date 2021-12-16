class Agenda:
    def __init__(self):
        self.dias = (Dia('Domingo'), Dia('Segunda'), Dia('Terça'), Dia('Quarta'),
                     Dia('Quinta'), Dia('Sexta'), Dia('Sábado'))
    

    def getDia(self, dia: int):
        return self.dias[dia]
    
    def getDias(self):
        return self.dias


class Dia:
    def __init__(self, nome: str):
        self.nome = nome
        self.tarefas = []

    def __repr__(self):
        return self.nome
    
    def getNome(self):
        return self.nome
    
    def getTarefas(self):
        return self.tarefas
    
    def addTarefa(self, nome: str):
        self.tarefas.append(nome)
    
    def removeTarefa(self, index: int):
        self.tarefa.pop(index)