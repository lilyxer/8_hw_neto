import json

with open('my_parser.json', encoding='utf-8') as file:
    d = json.load(file)
    print(len(set(d.keys())))
