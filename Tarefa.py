class Tarefa:
    def __init__(self, titulo: str, horario: str):
        self.__titulo = titulo      # Nome da tarefa
        self.__horario = horario    # Horário no formato XXhYY
    
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo: str):
        self.__titulo = titulo
    
    def get_horario(self):
        return self.__horario
    
    def set_horario(self, horario: str):
        self.__horario = horario