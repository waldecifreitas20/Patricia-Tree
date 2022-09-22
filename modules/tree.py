from modules.nodes.internNode import *
from modules.nodes.leaf import *
from modules import helper


class PatriciaTree:

    def __init__(self):
        self.nodes: int = 0
        self.root: Node = None

    def insert(self, word):

        # Caso 1: Arvore vazia
        if self.root == None:
            self.root = Leaf(word)
            return True

        else:
            node = self.root
            while True:

                # Caso 2: Node é folha
                if helper.isLeaf(node):

                    if node.value == word:
                        return False # Valor nao pode haver valores iguais na arvore
                    else:

                        nodeValue = node.value
                        index = helper.getMismatchIndex(nodeValue, word) #indice do primeiro caracter divergente

                        nodeChar = helper.getCharAtIndex(nodeValue, index) # caracter ja presente
                        wordChar = helper.getCharAtIndex(word, index)
                        char = helper.getSmaller(nodeChar, wordChar)

                        IS_ROOT = node.ancestor == None

                        if IS_ROOT:
                            self.root = InternNode(index, char)
                            node = self.root

                            if nodeChar > wordChar:
                                node.leftChild = Leaf(word)
                                node.rightChild = Leaf(nodeValue)

                            if nodeChar < wordChar:
                                node.leftChild = Leaf(nodeValue)
                                node.rightChild = Leaf(word)

                            node.rightChild.ancestor = node
                            node.leftChild.ancestor = node

                            return True

                        else:
                            IS_LEFT_CHILD = node.ancestor.leftChild.isEquals(node)
                  
                            if IS_LEFT_CHILD:
                                
                                node.ancestor.leftChild = InternNode(index, char)

                                if nodeChar > wordChar:
                                    node.ancestor.leftChild.leftChild = Leaf(word)
                                    node.ancestor.leftChild.rightChild = Leaf(nodeValue)

                                if nodeChar < wordChar:
                                    node.ancestor.leftChild.leftChild = Leaf(nodeValue)
                                    node.ancestor.leftChild.rightChild = Leaf(word)
                                  
                                node.ancestor.leftChild.leftChild.ancestor = node.ancestor.leftChild
                                node.ancestor.leftChild.rightChild.ancestor = node.ancestor.leftChild
                            else:
                                node.ancestor.rightChild = InternNode(index, char)

                                if nodeChar > wordChar:
                                    node.ancestor.rightChild.leftChild = Leaf(word)
                                    node.ancestor.rightChild.rightChild = Leaf(nodeValue)

                                if nodeChar < wordChar:
                                    node.ancestor.rightChild.leftChild = Leaf(nodeValue)
                                    node.ancestor.rightChild.rightChild = Leaf(word)
                                  
                                node.ancestor.rightChild.leftChild.ancestor = node.ancestor.rightChild
                                node.ancestor.rightChild.rightChild.ancestor = node.ancestor.rightChild

                            break
                else:
                    nodeChar = node.dismatchedChar

                    index = node.indexToGo
                    wordChar = helper.getCharAtIndex(word, index)

                    if wordChar > nodeChar:
                        node = node.rightChild
                    else:
                        node = node.leftChild



    def search(self, word):

        node = self.root

      
        while True:
        
            if helper.isLeaf(node):
                if node.value == word: 
                    return node
                else:
                    return -1
            
            else:
                index = node.indexToGo
                nodeChar = node.dismatchedChar
                wordChar = helper.getCharAtIndex(word, index)
                            
                if nodeChar < wordChar:
                    node = node.rightChild
                else:
                    node = node.leftChild


    def print(self):
        if self.root == None:
            print('Arvore Vazia')
        else:
            self._printTree(self.root, 'Root')

    def _printTree(self, node: Node, subtree):
        if Node is not None:          
            if helper.isLeaf(node):
                print(f'Node -> {node.value} | Path: {subtree} ')

            elif isinstance(node, InternNode):
                self._printTree(node.leftChild, subtree + ' -> left')
                self._printTree(node.rightChild, subtree + ' -> right')
