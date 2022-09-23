from modules.tree import PatriciaTree
from modules.menu import Menu

str1 = {'value' : 'a'}
str2 = str1
str1 = 'b'
str2 = str1
pt = PatriciaTree()
search = 'sal'
pt.insert('romane')

pt.print()
tela = Menu(pt)


acao = None
while True:
    if acao == None:
        tela.opcoes()
        acao = int(input("Opção:"))

    elif acao == 1:
        tela.clear_display()
        tela.opcoes()
        word = str(input("Digite sua palavra:"))
        pt.insert(word)
        acao = 4

    elif acao == 2:
        print("metodo NÂO IMPLEMENTADO")
        word = str(input("Qual palavra deseja remover:"))
        #pt.remove(word)

        tela.opcoes()
        acao = int(input("\nOpção:"))
        acao = None
    elif acao == 3:
        print("BuscaR")
        word = str(input("Qual palavra deseja BUSCAR:"))
        pt.search(word)
        print("metodo NÂO IMPLEMENTADO")
        acao = int(input("Digite 1 para voltar!"))
        acao = None
    elif acao == 4:
        pt.print()

        acao = int(input("Digite 1 para voltar!"))
        acao = None
    if acao == 0:
        break
#   -----FIM MENU------












