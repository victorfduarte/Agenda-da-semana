from Tarefa import Tarefa


class Dia:
    def __init__(self, num: int):
        self.__num: int = num    # Número do Dia
        self.__tarefas: list = []   # Lista de objetos Tarefa

    
    def get_num(self) -> int:
        '''Retorna o número que representa esse dia'''
        return self.__num
    
    def set_num(self, num: int):
        '''Seta o número que repesenta esse dia'''
        self.__num = num

    def get_tarefas(self) -> list:
        '''Retorna a lista de todas as tarefas do dia'''
        return self.__tarefas
    
    def add_tarefa(self, tarefa: Tarefa):
        '''Adiciona uma tarefa: Tarefa à lista de tarefas do dia'''
        self.__tarefas.append(tarefa)
    
    def remove_tarefa(self, tarefa: Tarefa):
        '''Remove uma tarefa: Tarefa da lista de tarefas do dia'''
        self.__tarefas.remove(tarefa)