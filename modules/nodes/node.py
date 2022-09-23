from abc import ABC, abstractmethod
from modules.nodes.internNode import *


class Node(ABC):
    def __init__(self):
        self.ancestor: InternNode = None
    

    def isEquals(self, node) -> bool:
        return id(self) == id(node)