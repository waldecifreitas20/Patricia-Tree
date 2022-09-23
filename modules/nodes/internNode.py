from modules.nodes.node import Node


class InternNode(Node):
    
    def __init__(self, indexToGo: int, dismatchedChar: str):
        self.indexToGo = indexToGo
        self.dismatchedChar = dismatchedChar
        self.leftChild = None
        self.rightChild = None
        super().__init__()


    def hasChildren(self) -> bool: return self.hasLeftChild() or self.hasRightChild()

    def hasLeftChild(self) -> bool: return self.left is not None

    def hasRightChild(self) -> bool: return self.right is not None

    def isLeftChild(self, node) -> bool: 
        return self.leftChild.isEquals(node)

    def isRightChild(self, node) -> bool: 
        return self.rightChild.isEquals(node)
