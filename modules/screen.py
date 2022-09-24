from modules.nodes.internNode import *
from modules.nodes.leaf import *
from modules import helper
from modules import tree
from os import (name as operationalSystem, system as command)

WINDOWNS = 'nt'

class Screen:

    def clearScreen(self):
        if operationalSystem == WINDOWNS:
            command('cls')
        else:
            command('clear')

    #Imprime um cabeçalho com a arvore atualizada e opções de menu
    def options(self, tree: tree):
        self.clearScreen()
        print("-------------------Arvore Patricia---------------------")
        print("Arvore atual: \n")
        self.printTree(tree)

        print("\033[0:30:47m[0]Encerar\033[m", end="")
        print("\033[0:32:40m[1]inserir\033[m", end="")
        if tree.root != None:
            print("\033[0:31:40m[2]Remover\033[m", end="")
            print("\033[0:33:40m[3]Buscar\033[m", end="")
        print("\033[0:36:40m[4]Ver Arvore\033[m")

    #imprime apenas a arvore(sem opções de menu)
    def printTree(self, tree: tree) -> None:
        self.clearScreen()
        print("-------------------Arvore Patricia---------------------")
        print("Arvore atual: \n")
        
        if tree.root == None:
            print('\033[0:31:40m***Arvore Vazia***\033[m')
        else:
            self._printTree(tree.root, 'Root')
        print("\n")

    def _printTree(self, node: Node, subtree) -> None:

        if Node is not None:

            if helper.isLeaf(node):
                print(f'Node -> {node.value} | Path: {subtree}  | Ancestor: {node.ancestor is not None}')

            elif isinstance(node, InternNode):
                print(
                    f'Node -> ({node.indexToGo},{node.dismatchedChar}) | Path: {subtree}  | Ancestor: {node.ancestor is not None}')
                self._printTree(node.leftChild, subtree + ' -> left')
                self._printTree(node.rightChild, subtree + ' -> right')
