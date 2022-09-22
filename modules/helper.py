from modules.nodes.leaf import Leaf


def getMismatchIndex(of: str, on: str) -> int:
    
    index = 0

    while index < len(of) and index < len(on):

        if of[index] != on[index]: 
            break
        index += 1

    return index

def getSmaller(str1, str2):
    return str1 if str1 < str2 else str2

def getCharAtIndex(str, index):
    try:
        return str[index]
    except:
        return ''

def isLeaf(node) -> bool: return isinstance(node, Leaf)