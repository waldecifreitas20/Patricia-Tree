from turtle import Screen
from modules.tree import PatriciaTree
from modules.screen import *

#objetos importantes para rodar o cod!
pt = PatriciaTree()
screen = Screen()
action = "13"
#-------

# -----Inicio MENU-----
while action != "0":
    #OBSERVAÇÃO: depois de executar uma opção(Remoção/busca), a usuario é redirecionado
    #para a tela HOME.

    #tela HOME
    if action == "13":
        screen.clearScreen()
        screen.options(pt)

        action = str(input("Opção:"))

        #tratamento de opçõe disponives para arvore vazia
        if (action == "2" or action == "3") and pt.root is None:
            action = "13"

    #Tela de inserção
    elif action == "1":
        while action == "1":

            screen.clearScreen()
            screen.printTree(pt)

            word = str(input("Qual palavra deseja \033[0:32:40mInserir\033[m:"))
            pt.insert(word)
            screen.clearScreen()

            print("Arvore Atual:")
            screen.printTree(pt)
            action = str(input("\n\033[0:30:47m[0]Voltar\033[m - \033[0:32:40m(1)Inserir\033[m outra palavra:"))

            #redirecionamento
            
            if action == "0":
                action = "13"
            elif action != "1":
                while action != "1" and action !="0":
                    print("Arvore Atual:")
                    screen.printTree(pt)
                    print('\n DIGITE UM VALOR VALIDO! \n')
                    action = str(input("\n\033[0:30:47m[0]Voltar\033[m - \033[0:32:40m(1)Inserir\033[m outra palavra:"))
            else:
                action = "1"

    #tela de remoção
    elif action == "2":
        while action == "2":
            screen.clearScreen()
            screen.printTree(pt)
            word = str(input("Qual palavra deseja \033[0:31:40mRemover\033[m:"))
            pt.remove(word)

            print("Arvore Atual:")
            screen.printTree(pt)
            if pt.root is not None:
                action = str(input("\n\033[0:30:47m[0]Voltar\033[m - \033[0:31:40m[1]Remover\033[m outra palavra:"))
            else:
                action = str(input("\n\033[0:30:47m[0]Voltar:\033[m "))

            # redirecionamento
            if action == "0":
                action = "13"
            elif action == "1":
                action = "2"
            else:
                action = "2"

    #tela de busca
    elif action == "3":
        while action == "3":
            screen.clearScreen()
            screen.printTree(pt)
            word = str(input("Qual palavra deseja \033[0:33:40mBuscar\033[m:"))

            print("Arvore Atual:")
            screen.printTree(pt)
            if pt.search(word) == -1:
                print("Retorno do metodo de BUSCA:", pt.search(word))
                print("Nó {", word, "} não encontrado!!!")
            else:
                print("Nó {", word, "} encontrado!!!")
                print("Retorno do metodo de BUSCA:", pt.search(word))

            action = str(input("\n\033[0:30:47m[0]Voltar\033[m - \033[0:33:40m[1]Buscar\033[m outra palavra:"))

            # redirecionamento
            if action == "0":
                action = "13"
            elif action == "1":
                action = "3"
            else:
                action = "3"

    #tela de visualização
    elif action == "4":
        screen.printTree(pt)

        # redirecionamento
        action = str(input("Aperte qualquer tecla para \033[0:30:47mVoltar\033[m!:"))
        action = "13"


#   -----FIM MENU------


screen.clearScreen()
print("-------Obrigado a todos!-------")
print("-------         <3      -------")












