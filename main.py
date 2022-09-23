import cmd

from modules.tree import PatriciaTree
from modules.menu import Menu

str1 = {'value' : 'a'}
str2 = str1
str1 = 'b'
str2 = str1
pt = PatriciaTree()
search = 'sal'

tela = Menu()

acao = 5
while acao != 0:

    tela.options(pt)
    acao = int(input("Opção:"))

    if acao == 1:
        word = str(input("Digite sua palavra:"))
        pt.insert(word)
        acao = 4

    elif acao == 2:
        print("metodo NÂO IMPLEMENTADO")
        word = str(input("Qual palavra deseja remover:"))
        pt.remove(word)
    elif acao == 3:

    elif acao == 4:


    if acao == 0:
        break
#   -----FIM MENU------












