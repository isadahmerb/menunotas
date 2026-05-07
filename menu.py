import os
import funcoes

notas = []

while True: 
    print("______________MENU______________")
    print("DIGITE 1 para adicionar nota \nDIGITE 2 para visualizar todas as notas \nDIGITE 3 para visualizar a média, a maior nota e a menor nota \nDIGITE 4 para salvar em um arquivo \nDIGITE 5 para sair")

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
            print("Digite o formato desejado: ")
            print("1.TXT")
            print("2.JSON")
            print("3.PLANILHA")
            formato = int(input())
            if formato == 1:
                funcoes.savetxt(notas)
            elif formato == 2:
                funcoes.savej(notas)
            elif formato == 3:
                funcoes.savep(notas)
        elif num == 5:
            break

    except ValueError:
        print("APENAS NUMEROS!")
    finally: 
        print("feito!")

