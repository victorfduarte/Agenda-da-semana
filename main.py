import os
import Agenda as Agenda
from Dia import Dia
from Tarefa import Tarefa
import Interface as ifc
from datetime import datetime


agenda = Agenda.Agenda("db.json")

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
dia_num = datetime.today().weekday()
hoje = dias_semana[dia_num]

dia: Dia = agenda.getDia(hoje)
tarefas: Tarefa = dia.get_tarefas()


def main():
    global dia, tarefas, dia_num, dias_semana

    menu_itens = ('Dia anterior', 'Dia posterior', 'Editar tarefas')

    while True:
        os.system('cls')
        ifc.cabecalho(dia.get_nome())
        ifc.space()
        ifc.lista_tarefas(tarefas, 1)
        ifc.space()
        ifc.line()
        ifc.space()
        ifc.lista_num(menu_itens, 1)
        ifc.space()

        op = int(input('Opção: '))
        if op == 1:
            # Decrementa o dia da semana
            if dia_num > 0: dia_num -= 1
            else: dia_num = 6
            dia = agenda.getDia(dias_semana[dia_num])
            tarefas = dia.get_tarefas()
        elif op == 2:
            if dia_num < 6: dia_num += 1
            else: dia_num = 0
            dia = agenda.getDia(dias_semana[dia_num])
            tarefas = dia.get_tarefas()
        elif op == 3:
            edit_day(dia)


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

main()
