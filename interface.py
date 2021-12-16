LINE_WIDTH = 30


def line():
    print('='*LINE_WIDTH)


def cabecalho(texto: str):
    line()
    print(texto.center(LINE_WIDTH))
    line()


def lista_num(itens: list, indent: int = 0):
    for n in range(1, len(itens)+1):
        print(' '*indent + f'{n}-{itens[n-1]}')


def lista(itens: list, indent: int = 0):
    for item in itens:
        print(' '*indent + f'{item}')