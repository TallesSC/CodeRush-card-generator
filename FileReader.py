import csv
import json


def readCSV(path):
    print("Lendo arquivo CSV...")
    rows = []
    with open(path, encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            rows.append({
                "baralho": row[0],
                "enunciado": row[1],
                "alternativa_a": row[2],
                "alternativa_b": row[3],
                "alternativa_c": row[4],
                "alternativa_d": row[5],
                "alternativa_e": row[6],
                "resposta": row[7],
                "dificuldade": row[8],
            })
    file.close()
    return rows


def readJSON(path):
    print("Lendo arquivo JSON...")
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    file.close()
    return data