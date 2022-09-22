from abc import ABC, abstractmethod
from modules.nodes.internNode import *


class Node(ABC):
    def __init__(self):
        self.ancestor: InternNode = None
    
    @abstractmethod
    def isEquals(self, node) -> bool:
        pass