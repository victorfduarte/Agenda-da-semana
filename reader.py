import json

def load(file_name: str) -> list:
    '''Lê um arquivo JSON'''
    with open(file_name, 'r') as file:
        text_json = json.loads(file.read())
    return text_json


def store(file_name: str, struct: list):
    '''Escreve em um arquivo JSON'''
    with open(file_name, 'w') as file:
        json.dump(struct, file)