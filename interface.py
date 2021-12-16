LINE_WIDTH = 30


def line():
    print('='*LINE_WIDTH)

def cabecalho(texto: str):
    line()
    print(texto.center(LINE_WIDTH))
    line()

def lista_num(itens: list):
    for n in range(1, len(itens)+1):
        print(f'{n} - {itens[n-1]}')