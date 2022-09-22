from modules.nodes.node import Node


class Leaf(Node):
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    def isEquals(self, node) -> bool:
        return node.value == self.value