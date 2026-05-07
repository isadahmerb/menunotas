import os
import json
import csv

def addnota(n):
    notas = []
    for i in range(n):
        print("Digite a nota:")
        notas.append(float(input()))
    return notas

def media(notas):
    if len(notas) == 0:
        print("Ainda nao possui notas!")
        return
    r = sum(notas) / len (notas)
    print(f"media = {r: .2f}")

def maior(notas):
    if len(notas) == 0:
        print("Ainda nao possui notas!")
        return
    r = max(notas) 
    print(f"maior = {r: .2f}")

def menor(notas):
    if len(notas) == 0:
        print("Ainda nao possui notas!")
        return
    r = min(notas) 
    print(f"menor = {r: .2f}")

def savetxt(notas):
    pasta = "notas"
    arquivo = "notas"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    caminho = os.path.join(pasta, arquivo)
    with open(caminho, "w") as f:
        f.write(f"notas : {notas}")

def savej(notas):
    pasta = "notas"
    arquivo = "notas.json"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho = os.path.join(pasta, arquivo)

    with open(caminho, "w") as f:
        json.dump(notas, f)

def savep(notas):
    base = os.path.dirname(os.path.abspath(__file__))
    pasta = os.path.join(base, "notas")

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho = os.path.join(pasta, "notas.csv")

    with open(caminho, "w") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(notas)

    print(f"salvo em : {caminho}")