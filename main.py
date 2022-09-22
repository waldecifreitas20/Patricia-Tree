from modules.tree import PatriciaTree


str1 = {'value' : 'a'}
str2 = str1

str1 = 'b'
str2 = str1

pt = PatriciaTree()

search = 'sal'

pt.insert('rubicon')
pt.insert('romanus')
pt.insert('romane')

pt.insert('rubens')
pt.insert('ruber')

pt.print()













