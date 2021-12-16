import os
import Agenda
import interface as ifc


agenda = Agenda.Agenda()

def main():
    menu_itens = ['Ver dias da semana', 'Editar dia', 'Sair']

    while True:
        os.system('cls')
        ifc.cabecalho('Agenda')
        print()
        ifc.lista_num(menu_itens)
        
        op = int(input('\nEscolha uma opção: '))
        if op == 1:
            show_days()
        elif op == 2:
            edit_day()
        elif op == 3:
            exit()


def show_days():
    menu_itens = ['Ver dias da semana', 'Editar dia', 'Sair']
    dia_num = 0
    dia = agenda.getDia(dia_num)


    while True:
        os.system('cls')
        ifc.cabecalho('Agenda')
        print()
        ifc.lista_num(menu_itens)


main()
        