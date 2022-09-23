import platform
from modules import tree
from modules.nodes.internNode import *
from modules.nodes.leaf import *
from modules import helper

so = platform.system()


class Menu:


    def cls(self):
        if so == 'Windows':
            print("WIN 10")
        elif so == 'Linux':
            print("LUnux")
        else:
            print("MAC")


    def print(tree: tree) -> None:

        if tree.root == None:
            print('Arvore Vazia')
        else:
            tree._printTree(tree.root, 'Root')

    def _printTree(self, node: Node, subtree) -> None:

        if Node is not None:

            if helper.isLeaf(node):
                print(f'Node -> {node.value} | Path: {subtree}  | Ancestor: {node.ancestor is not None}')

            elif isinstance(node, InternNode):
                print(
                    f'Node -> ({node.indexToGo},{node.dismatchedChar}) | Path: {subtree}  | Ancestor: {node.ancestor is not None}')
                self._printTree(node.leftChild, subtree + ' -> left')
                self._printTree(node.rightChild, subtree + ' -> right')
