from modules.tree import PatriciaTree


str1 = {'value' : 'a'}
str2 = str1

str1 = 'b'
str2 = str1

pt = PatriciaTree()

search = 'sal'


#   -----INICIO MENU------
opcao = None
while True:
    print("inicio laço!!!")
    if opcao == None:
        pt.menu()
        opcao = int(input("Opção:"))

    elif opcao == 1:
        pt.clear_display()

        print("Arvore atual: \n")
        pt.print()
        print("\n")
        palavra = str(input("Digite sua palavra:"))

        pt.clear_display()
        pt.insert(palavra)
        print("Arvore atual: \n")
        pt.print()
        print("\n")
        print("2 - Ver Arvore")
        print("1 - inserir")
        print("0 - Encerar")
        opcao = int(input("\nOpção:"))

    elif opcao == 2:
        pt.clear_display()
        print("Arvore atual: \n")
        pt.print()
        print("\n")
        print("1 - voltar")
        opcao = int(input("\nOpção:"))
        opcao = None
    if opcao == 0:
        break
#   -----FIM MENU------













