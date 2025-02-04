from flask import Flask, request
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

nome = list()
field_names = ['id', 'nome']


def id_sort(e):
    return e["id"]


@app.get('/nome')
def get_nome():
    nome.clear()
    with open("nome.csv", mode='r') as csv_name:
        name_csv = csv.DictReader(csv_name)
        for line in name_csv:
            nome.append(line)
    csv_name.close()
    return nome


@app.post('/nome')
def set_nome():
    row = list()
    new_nome = {'id': request.json['id'], 'nome': request.json['nome']}
    with open("nome.csv", newline='', mode='a') as csv_name:
        nome_csv = csv.DictWriter(csv_name, fieldnames=field_names)
        nome_csv.writerow(new_nome)
    csv_name.close()
    with open("nome.csv", mode='r') as csv_name:
        nome_csv = csv.DictReader(csv_name)
        for line in nome_csv:
            row.append(line)
        row.sort(key=id_sort)
    csv_name.close()
    with open("nome.csv", newline='', mode='w') as nome_csv:
        csv_name = csv.DictWriter(nome_csv, fieldnames=field_names)
        csv_name.writeheader()
        csv_name.writerows(row)
    nome_csv.close()
    return new_nome


@app.put('/nome')
def update_nome():
    row = list()
    up_nome = {'id': request.json['id'], 'nome': request.json['nome']}
    with open("nome.csv", mode='r') as csv_nome:
        nome_csv = csv.DictReader(csv_nome, fieldnames=field_names)
        for line in nome_csv:
            if line["id"] == up_nome["id"]:
                row.append(up_nome)
            else:
                row.append(line)
    csv_nome.close()
    with open("nome.csv", newline='', mode='w') as nome_csv:
        csv_nome = csv.DictWriter(nome_csv, fieldnames=field_names)
        csv_nome.writerows(row)
    return row


@app.delete('/nome')
def delete_nome():
    row = list()
    dlt_nome = {'id': request.json['id'], 'nome': request.json['nome']}
    with open("nome.csv", mode='r') as nome_csv:
        csv_name = csv.DictReader(nome_csv)
        for line in csv_name:
            if line != dlt_nome:
                row.append(line)
    nome_csv.close()
    with open("nome.csv", newline='', mode='w') as nome_csv:
        csv_name = csv.DictWriter(nome_csv, fieldnames=field_names)
        csv_name.writeheader()
        csv_name.writerows(row)
    nome_csv.close()

    return dlt_nome


app.run()
