import os

from modules.nodes.internNode import *
from modules.nodes.leaf import *
from modules import helper
from modules import tree
import platform


so = platform.system()


class Menu:
    def cls(self):

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #if so == 'Windows':
        #    os.system('clear')
        #elif so == 'Linux':
         #   os.system('cls') or None
        #else:
        #    os.system('cls') or None

    def options(self, tree: tree):
        self.cls()
        print("---------------Arvore Patricia-------------------")
        print("Arvore atual: \n")
        self.print(tree)

        print("3 - Buscar")
        print("2 - Remover")
        print("1 - inserir")
        print("0 - Encerar\n")

    def print(self, tree: tree) -> None:

        if tree.root == None:
            print('Arvore Vazia')
        else:
            self._printTree(tree.root, 'Root')

    def _printTree(self, node: Node, subtree) -> None:

        if Node is not None:

            if helper.isLeaf(node):
                print(f'Node -> {node.value} | Path: {subtree}  | Ancestor: {node.ancestor is not None}')

            elif isinstance(node, InternNode):
                print(
                    f'Node -> ({node.indexToGo},{node.dismatchedChar}) | Path: {subtree}  | Ancestor: {node.ancestor is not None}')
                self._printTree(node.leftChild, subtree + ' -> left')
                self._printTree(node.rightChild, subtree + ' -> right')
