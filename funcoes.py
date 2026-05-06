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
