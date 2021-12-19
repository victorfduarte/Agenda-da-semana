from Tarefa import Tarefa


class Dia:
    def __init__(self, num: int):
        self.__num: int = num    # Número do Dia
        self.__tarefas: list = []   # Lista de objetos Tarefa

    
    def get_num(self) -> int:
        return self.__num
    
    def set_num(self, num: int):
        self.__num = num

    def get_tarefas(self) -> list:
        return self.__tarefas
    
    def add_tarefa(self, tarefa: Tarefa):
        self.__tarefas.append(tarefa)
    
    def remove_tarefa(self, tarefa: Tarefa):
        self.__tarefas.remove(tarefa)