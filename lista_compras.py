lista = ["Leite", "Morango", "Pasta de Dente"]

def mostrar():
    print(lista)
def cadastrar():
    item = str(input("Digite o item que quer cadastrar:")).title()
    lista.append(item)
    print(lista)
def excluir():
    print(lista)
    remove = str(input("Qual item da lista deseja remover? "))
    lista.remove(remove)
    print(lista)
def modificar():
    print(lista)
    modify = int(input("Qual item deseja alterar? "))
    alteração = str(input("Pelo oque deseja substituir? "))
    lista[modify] = alteração
    print(lista)

print("================")
print("Lista de Compras")
print("================")
print("1. Mostrar Lista")
print("2. Cadastrar Item")
print("3. Excluir Item")
print("4. Modificar Item")
print("0. Sair")

escolha = int(input("Digite a opção: "))

while True:
    if escolha == 1:
        mostrar()
        escolha = int(input("Digite a opção: "))
    if escolha == 2:
        cadastrar()
        escolha = int(input("Digite a opção: "))
    if escolha == 3:
        excluir()
        escolha = int(input("Digite a opção: "))
    if escolha == 4:
        modificar()
        escolha = int(input("Digite a opção: "))
    if escolha == 0:
        print("Finalizando programa...")
        break