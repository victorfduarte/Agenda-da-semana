import os
import classes.Agenda as Agenda
import classes.interface as ifc


agenda = Agenda.Agenda("db.json")

'''
agenda.getDia(0).addTarefa('Acordar cedo')

def main():
    menu_itens = ('Ver dias da semana', 'Sair')

    while True:
        os.system('cls')
        ifc.cabecalho('Agenda')
        print()
        ifc.lista_num(menu_itens, 1)
        # print()
        # ifc.line()
        
        op = int(input('\nEscolha uma opção: '))
        if op == 1:
            show_days()
        elif op == 2:
            exit()


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
'''