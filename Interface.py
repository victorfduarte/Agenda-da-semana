from typing import Generator, List
from Tarefa import Tarefa
import os


LINE_WIDTH = 30


def line():
    '''Desenha uma linha com o símbolo ='''
    print('='*LINE_WIDTH)


def clear():
    os.system('cls')


def cabecalho(texto: str):
    '''Desenha um cabeçalho'''
    line()
    print()
    print(texto.center(LINE_WIDTH))
    print()
    line()


def space():
    '''Imprime uma linha de espaço em branco'''
    print()


def lista_num(itens: list, indent: int = 0):
    '''Imprime itens em forma de uma lista numerada'''
    for n in range(1, len(itens)+1):
        print(' '*indent + f'({n}) {itens[n-1]}')


def lista(itens: list, indent: int = 0):
    '''Imprime em forma de uma lista'''
    for item in itens:
        print(' '*indent + f'{item}')


def lista_tarefas(func_itens: None, indent: int = 0):
    '''Imprime elementos do tipo tarefa em forma de lista'''
    for item in func_itens():
        print(' '*indent + f'{item.get_horario()}  {item.get_titulo()}')
        print()