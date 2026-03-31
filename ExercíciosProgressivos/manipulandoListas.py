#lista com termo faltando
lista = [1,2,4,5]
#adicione o 3, para que o padrão se mantenha
lista.insert(2,3)
#exiba a lista
print(lista)
#adicione 3 elementos ao final da lista
novos3 = [6,7,8]
lista.extend(novos3)
#exiba a lista
print(lista)
#some os valores da lista
soma = 0
soma2 = 0

for i in lista:
    soma = soma+i
#exiba a soma
print("Soma: ", soma)
#usuário deve inserir um valor na lista
novoValor = input("NOVO VALOR: ")
#se for um digito, some, caso o contrario exiba a lista
if novoValor.isdigit():
    lista.append(int(novoValor))
    print(sum(lista))
    print(lista)
else:
    lista.append(novoValor)
    print(lista)

        