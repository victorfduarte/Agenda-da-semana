import os
import Agenda as Agenda
from Dia import Dia
from Tarefa import Tarefa
import Interface as ifc
from datetime import datetime


class AgendaSemana:
    def __init__(self):
        self.__dias_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

        self.__agenda = Agenda.Agenda("db.json")
        self.__dia_num = 6  # datetime.today().weekday() - 1
        self.__dia: Dia = self.__agenda.getDia(self.__dia_num)


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

            op = int(input('Opção: '))
            if op == 1:
                # Decrementa o dia da semana
                self.incDay()
                self.updateDay()
            elif op == 2:
                # Incrementa o dia da semana
                self.decDay()
                self.updateDay()
            elif op == 3:
                # edit_day(dia)
                pass
    

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
        '''Atualiza o objeto que representa o dia'''
        self.__dia = self.__agenda.getDia(self.__dia_num)
    

    def textDay(self) -> str:
        '''Retorna a string que representa o dia atual'''
        return self.__dias_semana[self.__dia_num]
    

    def get_tarefa(self):
        for t in self.__dia.get_tarefas():
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
