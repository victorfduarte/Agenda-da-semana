import json

def load(base_file):
    with open(base_file, 'r') as file:
        text_json = json.loads(file.read())
    return text_json