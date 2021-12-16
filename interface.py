LINE_WIDTH = 30


def line():
    print('='*LINE_WIDTH)

def cabecalho(texto: str):
    line()
    print(texto.center(LINE_WIDTH))
    line()

