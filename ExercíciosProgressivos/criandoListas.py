#criando lista
lista = ["banana", "morango", "leite", "cenoura", "arroz"]
#exibindo elementos da lista
for i in range(len(lista)):
    print(lista[i])
#usuário adiciona 3 items na lista
for i in range(3):
    novoItem = input("Digite um novo item: ").lower()
    lista.append(novoItem)
#exibindo lista nova
print(lista)
#utilizando funções de manipulação de listas
lista.pop(2)
print(lista)

