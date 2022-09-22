from modules import tree

class Menu():
    def opcoes(self):
        self.clear_display()
        print("---------------Arvore Patricia-------------------")
        print("Arvore atual: \n")
        self.tree_print()
        print("\n")
        print("4 - Ver Arvore")
        print("3 - Buscar")
        print("2 - Remover")
        print("1 - inserir")
        print("0 - Encerar\n")

    def clear_display(self):
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")

    def tree_print(self):
        print("Arvore atual: \n")

        print("\n")

