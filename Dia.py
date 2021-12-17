from Tarefa import Tarefa


class Dia:
    def __init__(self, nome: str):
        self.__nome = nome    # Nome do Dia
        self.__tarefas = []   # Lista de objetos Tarefa

    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome: str):
        self.__nome = nome

    def get_tarefas(self):
        return self.__tarefas
    
    def add_tarefa(self, tarefa: Tarefa):
        self.__tarefas.append(tarefa)
    
    def remove_tarefa(self, tarefa: Tarefa):
        self.__tarefas.remove(tarefa)