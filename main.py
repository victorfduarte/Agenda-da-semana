import os
import Agenda
import interface as ifc


agenda = Agenda.Agenda()
agenda.getDia(0).addTarefa('Acordar cedo')

def main():
    menu_itens = ['Ver dias da semana', 'Editar dia', 'Sair']

    while True:
        os.system('cls')
        ifc.cabecalho('Agenda')
        print()
        ifc.lista_num(menu_itens, 1)
        print()
        ifc.line()
        
        op = int(input('\nEscolha uma opção: '))
        if op == 1:
            show_days()
        elif op == 2:
            edit_day()
        elif op == 3:
            exit()


def show_days():
    dia_num = 0
    dia = agenda.getDia(dia_num)
    menu_itens = dia.getTarefas()

    while True:
        os.system('cls')
        ifc.cabecalho(dia.getNome())
        print()
        ifc.lista(menu_itens, 1)
        print()
        ifc.line()
        print()
        ifc.lista(('(a) Dia anterior', '(p) Dia posterior', 'Enter para sair'))

        op = input(': ')
        if op == '':
            return
        elif op == 'a':
            pass
        elif op == 'p':
            pass


main()
        