from modules.nodes.node import Node


class Leaf(Node):
    def __init__(self, value):
        self.value = value
        super().__init__()
    