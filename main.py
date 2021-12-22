import os
import reader
import Agenda as Agenda
from Dia import Dia
from Tarefa import Tarefa
import Interface as ifc
from datetime import datetime


class AgendaSemana:
    def __init__(self):
        self.__dias_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

        struct = reader.load("db.json")
        self.__agenda = Agenda.Agenda(struct)

        self.__dia_num = datetime.today().weekday()
        self.incDay()
        self.__dia_atual: Dia = self.__agenda.getDia(self.__dia_num)


    def run(self):
        menu_itens = ('Dia posterior', 'Dia anterior', 'Editar tarefas')

        while True:
            os.system('cls')
            ifc.cabecalho(self.textDay())
            ifc.space()
            ifc.lista_tarefas(self.get_tarefa, 1)
            ifc.line()
            ifc.space()
            ifc.lista_num(menu_itens, 1)
            ifc.space()

            op = input('Opção: ')
            if not op:
                continue

            op = int(op)
            if op == 1:
                # Decrementa o dia da semana
                self.incDay()
                self.updateDay()
            elif op == 2:
                # Incrementa o dia da semana
                self.decDay()
                self.updateDay()
            elif op == 3:
                # Editar tarefas
                self.telaEditarTarefas()
    

    def telaEditarTarefas(self):
        menu_itens = ('Nova tarefa', 'Remover tarefa', 'Editar tarefa')

        while True:
            ifc.clear()
            ifc.cabecalho(self.textDay())
            ifc.space()
            ifc.lista_tarefas(self.get_tarefa, 1)
            ifc.line()
            ifc.space()
            ifc.lista_num(menu_itens, 1)
            ifc.space()

            op = input('Opção (Enter pra voltar): ')
            if not op:
                return

            op = int(op)
            if op == 1:
                # Nova Tarefa
                self.telaNovaTarefa()
            elif op == 2:
                # Remover Tarefa
                self.telaImplementar("Tela de Remoção ainda não foi implementada\n\nEnter para voltar")
            elif op == 3:
                # Editar tarefa
                self.telaImplementar("Tela de Edição ainda não foi implementada\n\nEnter para voltar")
    

    def telaNovaTarefa(self):
        ifc.clear()
        ifc.cabecalho(self.textDay())
        ifc.space()

        while True:
            titulo = input(' '*4 + 'Titulo: ')
            horario = input(' '*4 + 'Horario: ')
            print()

            print(' '*4 + 'Tem certeza de todas as informações?')
            confirm = input(' '*4 + '(enter - sim, r - refazer, c - cancelar): ').lower()
            
            if confirm == '':
                tarefa = Tarefa(titulo, horario)
                self.addTarefa(tarefa)
                return
            elif confirm == 'r':
                ifc.clear()
                continue
            elif confirm == 'c':
                return



    def telaImplementar(self, msg):
        ifc.clear()
        input(msg)
    

    def addTarefa(self, tarefa: Tarefa):
        '''Adiciona uma tarefa à lista de tarefas do dia atual e atualiza a base de dados'''
        self.__dia_atual.add_tarefa(tarefa)
        
        if self.__dia_atual not in self.__agenda.getDias():
            self.__agenda.addDia(self.__dia_atual)

        reader.store("db.json", self.convertStruct())
    

    def convertStruct(self) -> list:
        dias = self.__agenda.getDias()
        struct = []

        for d in dias:
            dia = {'dia': d.get_num(), 'tarefas': []}

            for t in d.get_tarefas():
                tarefa = {"titulo": t.get_titulo(), "horario": t.get_horario()}
                dia["tarefas"].append(tarefa)

            struct.append(dia)
        
        return struct

    

    def incDay(self):
        '''Incrementa a variável que representa o dia em forma numérica'''
        if self.__dia_num < 6:
            self.__dia_num += 1
        else:
            self.__dia_num = 0


    def decDay(self):
        '''Decrementa a variável que representa o dia em forma numérica'''
        if self.__dia_num > 0:
            self.__dia_num -= 1
        else:
            self.__dia_num = 6
    

    def updateDay(self):
        '''Atualiza o objeto que representa o dia atual'''
        self.__dia_atual = self.__agenda.getDia(self.__dia_num)
    

    def textDay(self) -> str:
        '''Retorna a string que representa o dia atual'''
        return self.__dias_semana[self.__dia_num]
    

    def get_tarefa(self):
        for t in self.__dia_atual.get_tarefas():
            yield t

'''
def show_days():
    dia_num = 0
    dia = agenda.getDia(dia_num)
    tarefas = dia.getTarefas()
    menu_itens = ('[a] Dia anterior', '[p] Dia posterior', '[e] Editar tarefas','    Enter para sair')

    while True:
        os.system('cls')
        ifc.cabecalho(dia.getNome())
        print()
        ifc.lista(tarefas, 1)
        print()
        ifc.line()
        print()
        ifc.lista(menu_itens, 1)

        op = input('\nOpção: ')
        if op == '':
            return
        elif op == 'a':
            if dia_num > 0: dia_num -= 1
            else: dia_num = 6
            dia = agenda.getDia(dia_num)
            tarefas = dia.tarefas
        elif op == 'p':
            if dia_num < 6: dia_num += 1
            else: dia_num = 0
            dia = agenda.getDia(dia_num)
            tarefas = dia.tarefas
        elif op == 'e':
            edit_day(dia)


def edit_day(dia):
    tarefas = dia.getTarefas()
    menu_itens = ('[a] Acrescentar tarefa', '[r] Remover tarefa', '    Enter para sair')

    while True:
        os.system('cls')
        ifc.cabecalho(dia.getNome())
        print()
        ifc.lista(tarefas, 1)
        print()
        ifc.line()
        print()
        ifc.lista(menu_itens, 1)

        op = input('\nOpção: ')
        if op == '':
            return
        elif op == 'a':
            acrescentar_tarefa(dia)
        elif op == 'r':
            remover_tarefa(dia)


def acrescentar_tarefa(dia):
    os.system('cls')
    ifc.cabecalho('Adicionar Tarefa')
    print()
    nome = input('Nome da tarefa: ')
    horario = input('Horário (XXhYY): ')

    dia.addTarefa(nome)


def remover_tarefa(dia):
    os.system('cls')
    ifc.cabecalho('Remover Tarefa')
    print()
    nome = input('Nome da tarefa: ')

    dia.removeTarefa(nome)
'''

agenda = AgendaSemana()
agenda.run()


'''
print(agenda.convertStruct())
print(agenda._AgendaSemana__agenda.getDias())
'''