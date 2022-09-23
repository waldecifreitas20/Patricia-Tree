from modules.nodes.internNode import *
from modules.nodes.leaf import *
from modules import helper


class PatriciaTree:

    def __init__(self):
        self.nodes: int = 0
        self.root: Node = None

    def insert(self, word) -> bool:

        # Caso a arvore esteja vazia a palavra é inserida na raiz
        if self.root == None:
            self.root = Leaf(word)
            return True

        else:
            currentNode = self.root
            while True:

                # Verifica se o Nó é folha
                if helper.isLeaf(currentNode):

                    if currentNode.value == word:
                        return False  # Nao podem haver valores iguais na arvore
                    else:

                        nodeValue = currentNode.value

                        # indice do primeiro caracter divergente
                        index = helper.getMismatchIndex(nodeValue, word)

                        # Obtem os caracteres divergentes
                        nodeChar = helper.getCharAtIndex(nodeValue, index)
                        wordChar = helper.getCharAtIndex(word, index)

                        char = helper.getSmaller(nodeChar, wordChar)

                        IS_ROOT = currentNode.ancestor == None

                        # Verfica se o Nó atual é raiz da arvore
                        if IS_ROOT:

                            # Nó raiz vira Nó interno
                            self.root = InternNode(index, char)

                            # Define as novas palavras como filhas folha da raiz
                            if nodeChar < wordChar:
                                self.root.leftChild = Leaf(nodeValue)
                                self.root.rightChild = Leaf(word)
                            else:
                                self.root.leftChild = Leaf(word)
                                self.root.rightChild = Leaf(nodeValue)

                            # Define a raiz como pai das novas folhas
                            self.root.rightChild.ancestor = self.root
                            self.root.leftChild.ancestor = self.root

                            return True

                        else:
                            # Pai do no atual
                            ancestor = currentNode.ancestor

                            IS_LEFT_CHILD = ancestor.leftChild.isEquals(
                                currentNode)

                            # verifica se o Nó atual esta a esquerda de seu pai
                            if IS_LEFT_CHILD:

                                # Nó atual vira Nó interno
                                ancestor.leftChild = InternNode(index, char)

                                # Nó atual
                                currentNode = ancestor.leftChild

                                # Define as novas palavras como filhas folhas do Nó
                                if nodeChar >= wordChar:
                                    currentNode.leftChild = Leaf(word)
                                    currentNode.rightChild = Leaf(nodeValue)
                                else:
                                    currentNode.leftChild = Leaf(nodeValue)
                                    currentNode.rightChild = Leaf(word)

                                # Define o pai das novas folhas
                                currentNode.leftChild.ancestor = currentNode
                                currentNode.rightChild.ancestor = currentNode

                            else:  # Filho esta a direita de seu pai

                                # Nó atual vira Nó interno
                                ancestor.rightChild = InternNode(index, char)

                                # Nó atual
                                currentNode = ancestor.rightChild

                                # Define as novas palavras como filhas folhas do Nó
                                if nodeChar > wordChar:
                                    currentNode.leftChild = Leaf(word)
                                    currentNode.rightChild = Leaf(nodeValue)
                                else:
                                    currentNode.leftChild = Leaf(nodeValue)
                                    currentNode.rightChild = Leaf(word)

                                # Define o pai das novas folhas
                                currentNode.leftChild.ancestor = currentNode
                                currentNode.rightChild.ancestor = currentNode

                            break

                else:  # Nó atual é interno

                    index = currentNode.indexToGo
                    nodeChar = currentNode.dismatchedChar
                    wordChar = helper.getCharAtIndex(word, index)

                    # Define para qual lado da arvore seguir
                    if wordChar > nodeChar:
                        currentNode = currentNode.rightChild
                    else:
                        currentNode = currentNode.leftChild

    # Retorna o Nó da arvore caso encontre ou -1 caso o Nó nao exista

    def search(self, word) -> Node or -1:

        node = self.root

        while True:
            # Verifica se o No é folha
            if helper.isLeaf(node):
                if node.value == word:
                    return node
                else:
                    return -1

            else:
                # Caso o Nó atual seja interno o algoritmo continua a busca
                index = node.indexToGo
                nodeChar = node.dismatchedChar
                wordChar = helper.getCharAtIndex(word, index)

                # Verfica qual direcao da arvore ir
                if nodeChar < wordChar:
                    node = node.rightChild
                else:
                    node = node.leftChild

    def remove(self, word):
        nodeSearched = self.search(word)

        if nodeSearched == -1:
            return False

        ancestor = nodeSearched.ancestor

        # Caso Nó removido seja raiz
        if nodeSearched.isEquals(self.root):
            self.root = None

        # Caso o pai do Nó removido seja raiz
        elif ancestor.isEquals(self.root):
            IS_LEFT_CHILD = ancestor.isLeftChild(nodeSearched)

            if IS_LEFT_CHILD:  # No removido esta a esquerda de seu pai
                ancestor.leftChild = None
                ancestor = ancestor.rightChild

            else:  # No removido esta a direita de seu pai
                ancestor.rightChild = None
                ancestor = ancestor.leftChild

            ancestor.ancestor = None
        
        else:
            IS_LEFT_CHILD = ancestor.isLeftChild(nodeSearched)


    def print(self) -> None:

        if self.root == None:
            print('Arvore Vazia')
        else:
            self._printTree(self.root, 'Root')

    def _printTree(self, node: Node, subtree) -> None:

        if Node is not None:

            if helper.isLeaf(node):
                print(
                    f'Node -> {node.value} | Path: {subtree}  | Ancestor: {node.ancestor is not None}')

            elif isinstance(node, InternNode):
                self._printTree(node.leftChild, subtree + ' -> left')
                self._printTree(node.rightChild, subtree + ' -> right')
