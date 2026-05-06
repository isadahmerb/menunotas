import funcoes

notas = []

while True: 
    print("______________MENU______________")
    print("DIGITE 1 para adicionar nota \nDIGITE 2 para visualizar todas as notas \nDIGITE 3 para visualizar a média, a maior nota e a menor nota \nDIGITE 4 para sair ")

    try:    
        num = int(input())

        if num == 1:
            print("quantas notas serao adicionadas? ")
            n = int(input())
            notas = funcoes.addnota(n)
        elif num == 2:
            print(notas)
        elif num == 3:
            funcoes.media(notas)
            funcoes.maior(notas)
            funcoes.menor(notas)
        elif num == 4:
            break

    except ValueError:
        print("APENAS NUMEROS!")
    finally: 
        print("feito!")

