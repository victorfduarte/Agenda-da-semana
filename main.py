import os
import Agenda
import interface as ifc


agenda = Agenda.Agenda()
agenda.getDia(0).addTarefa('Acordar cedo')

def main():
    menu_itens = ('Ver dias da semana', 'Editar dia', 'Sair')

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
    tarefas = dia.getTarefas()
    menu_itens = ('[a] Dia anterior', '[p] Dia posterior', '[e] Editar farefas','    Enter para sair')

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


main()
        