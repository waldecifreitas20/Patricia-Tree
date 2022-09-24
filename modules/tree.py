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
                                
                                # Atualiza valores Nó atual
                                currentNode = ancestor.leftChild
                                currentNode.ancestor = ancestor

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

                                # Atualiza valores Nó atual
                                currentNode = ancestor.rightChild
                                currentNode.ancestor = ancestor

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

    def remove(self, word) -> bool:
        nodeSearched = self.search(word)

        # Nó nao existe
        if nodeSearched == -1:
            return False

        ancestor = nodeSearched.ancestor

        # Caso Nó removido seja raiz
        if nodeSearched.isEquals(self.root):
            self.root = None

        # Caso o pai do Nó removido seja raiz
        elif ancestor.isEquals(self.root):
            IS_LEFT_CHILD = self.root.isLeftChild(nodeSearched)

            # Remove o Nó e raiz recebe Nó sucessor
            if IS_LEFT_CHILD:  
                self.root.leftChild = None
                self.root = self.root.rightChild

            else:
                self.root.rightChild = None
                self.root = self.root.leftChild

            self.root.ancestor = None

      
        else:
            IS_LEFT_CHILD = ancestor.isLeftChild(nodeSearched)

            # No removido esta a esquerda de seu pai
            if IS_LEFT_CHILD:
                # Remove o Nó
                ancestor.leftChild = None
                # Avo do Nó removido
                grandFather = ancestor.ancestor
                # Nó sucessor recebe novo pai
                ancestor.rightChild.ancestor = grandFather
                
                # Avo do Nó removido aponta para o novo filho
                if grandFather.isLeftChild(ancestor):
                    grandFather.leftChild = ancestor.rightChild                    
                else:
                    grandFather.rightChild = ancestor.rightChild
            else:
                # Remove o Nó
                ancestor.rightChild = None
                # Avo do Nó removido
                grandFather = ancestor.ancestor
                # Nó sucessor recebe novo pai
                ancestor.leftChild.ancestor = grandFather
                
                # Avo do Nó removido aponta para o novo filho
                if grandFather.isLeftChild(ancestor):
                    grandFather.leftChild = ancestor.leftChild                    
                else:
                    grandFather.rightChild = ancestor.leftChild
        return True

