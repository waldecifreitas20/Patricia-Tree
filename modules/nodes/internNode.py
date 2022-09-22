from modules.nodes.node import Node


class InternNode(Node):
    
    def __init__(self, indexToGo: int, dismatchedChar: str):
        self.indexToGo = indexToGo
        self.dismatchedChar = dismatchedChar
        self.leftChild = None
        self.rightChild = None
        super().__init__()

    def isEquals(self, node) -> bool:
        return super().isEquals(node)

    def hasChildren(self) -> bool: return self.hasLeftChild() or self.hasRightChild()

    def hasLeftChild(self) -> bool: return self.left is not None

    def hasRightChild(self) -> bool: return self.right is not None

    def getLength(self) -> int: return len(self.value)
